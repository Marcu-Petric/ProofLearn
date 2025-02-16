from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Section, Question
from .forms import CourseForm, SectionWithQuestionsForm, FinalExamForm
import json

def course_list(request):
    courses = Course.objects.all()  # Get all courses
    return render(request, 'courses/display_courses.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    sections = course.sections.all()  # Get all sections for this specific course
    return render(request, 'courses/individual_course.html', {
        'course': course,
        'sections': sections
    })

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('courses:course_detail', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

def create_section(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = SectionWithQuestionsForm(request.POST)
        if form.is_valid():
            # Create Section
            section = Section.objects.create(
                name=form.cleaned_data['section_name'],
                content_path=form.cleaned_data['content_path'],
                course=course
            )

            # Create Section Questions
            for i in range(1, 3):  # Assuming you have 2 questions
                # Split the variants by comma and strip whitespace
                variants = [variant.strip() for variant in form.cleaned_data[f'question{i}_variants'].split(',')]
                
                Question.objects.create(
                    text=form.cleaned_data[f'question{i}_text'],
                    variants=variants,  # Store the list of variants
                    correct_variant=form.cleaned_data[f'question{i}_correct'],
                    section=section
                )

            return redirect('courses:course_detail', course_id=course_id)
    else:
        form = SectionWithQuestionsForm()
    return render(request, 'courses/add_section.html', {'form': form, 'course': course})

def create_final(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = FinalExamForm(request.POST)
        if form.is_valid():
            # Create Final Questions
            for i in range(1, 11):  # 10 questions
                Question.objects.create(
                    text=form.cleaned_data[f'question{i}_text'],
                    variants=json.loads(form.cleaned_data[f'question{i}_variants']),
                    correct_variant=form.cleaned_data[f'question{i}_correct'],
                    course=course,
                    is_final=True
                )

            return redirect('courses:course_detail', course_id=course_id)
    else:
        form = FinalExamForm()
    return render(request, 'courses/add_final.html', {'form': form, 'course': course})

