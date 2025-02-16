from django import forms
from .models import Course, Section, Question

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'passing_points', 'category']

class SectionWithQuestionsForm(forms.Form):
    section_name = forms.CharField(max_length=255)
    content_path = forms.CharField(max_length=255)

    # First question
    question1_text = forms.CharField(widget=forms.Textarea)
    question1_variants = forms.CharField(widget=forms.Textarea)
    question1_correct = forms.CharField()

    # Second question
    question2_text = forms.CharField(widget=forms.Textarea)
    question2_variants = forms.CharField(widget=forms.Textarea)
    question2_correct = forms.CharField()

class FinalExamForm(forms.Form):
    question1_text = forms.CharField(widget=forms.Textarea)
    question1_variants = forms.CharField(widget=forms.Textarea)
    question1_correct = forms.CharField()

    question2_text = forms.CharField(widget=forms.Textarea)
    question2_variants = forms.CharField(widget=forms.Textarea)
    question2_correct = forms.CharField()

    question3_text = forms.CharField(widget=forms.Textarea)
    question3_variants = forms.CharField(widget=forms.Textarea)
    question3_correct = forms.CharField()

    question4_text = forms.CharField(widget=forms.Textarea)
    question4_variants = forms.CharField(widget=forms.Textarea)
    question4_correct = forms.CharField()

    question5_text = forms.CharField(widget=forms.Textarea)
    question5_variants = forms.CharField(widget=forms.Textarea)
    question5_correct = forms.CharField()

    question6_text = forms.CharField(widget=forms.Textarea)
    question6_variants = forms.CharField(widget=forms.Textarea)
    question6_correct = forms.CharField()

    question7_text = forms.CharField(widget=forms.Textarea)
    question7_variants = forms.CharField(widget=forms.Textarea)
    question7_correct = forms.CharField()

    question8_text = forms.CharField(widget=forms.Textarea)
    question8_variants = forms.CharField(widget=forms.Textarea)
    question8_correct = forms.CharField()

    question9_text = forms.CharField(widget=forms.Textarea)
    question9_variants = forms.CharField(widget=forms.Textarea)
    question9_correct = forms.CharField()

    question10_text = forms.CharField(widget=forms.Textarea)
    question10_variants = forms.CharField(widget=forms.Textarea)
    question10_correct = forms.CharField()


