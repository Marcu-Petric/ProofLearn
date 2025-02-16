// Learning App Model Checker
// Based on actual Django implementation in courses/

dtmc

// Global constants
const int MAX_SECTIONS = 3;  // Maximum number of sections in a course
const int FINAL_SECTION = 4; // Special state for final exam
const int QUESTIONS_PER_SECTION = 2;  // From create_section view
const int FINAL_QUESTIONS = 10;  // From create_final view
const int MIN_POINTS_TO_PASS = 7;  // Example passing threshold

// Module for tracking user state and course progress
module UserState
    // Authentication state (from @login_required decorator)
    auth : [0..1] init 0;  // 0=not authenticated, 1=authenticated
    
    // Enrollment state (from UserProgress model)
    enrolled : [0..1] init 0;  // Start not enrolled
    
   // Track if course is created
    course_created : [0..1] init 0;

    // Current section tracking (from UserProgress.section)
    current_section : [0..FINAL_SECTION] init 0;
    
    // Question answers tracking (for section completion)
    correct_answers : [0..2] init 0;  // For current section's questions
    
    // Final exam points (for course completion)
    final_points : [0..10] init 0;
    
    // Track if final exam is in progress
    final_exam_in_progress : [0..1] init 0;
    
    // Track if answers are submitted
    answers_submitted : [0..1] init 0;
    
    // Track if course has sections
    has_sections : [0..1] init 0;  // Initialize to 0 (no sections at start)
    
    // Add progress tracking
    progress_saved : [0..1] init 0;
    previous_section : [0..MAX_SECTIONS] init 0;
    
    
    // Login/Logout transitions - MODIFIED
    [] auth=0 & enrolled=0 & course_created=0 -> (auth'=1);
    [] auth=1 -> (auth'=0) & (correct_answers'=0) & (final_exam_in_progress'=0) & 
        (final_points'=0) & (current_section'=0) & (enrolled'=0) & (course_created'=0) & 
        (has_sections'=0);
    
    // Enrollment - MODIFIED
    [] auth=1 & enrolled=0 & current_section=0 & has_sections=1 & final_exam_in_progress=0 -> 
        (enrolled'=1) & (current_section'=1);
    
    // Section progression (mutually exclusive with final exam)
    [] enrolled=1 & current_section>0 & current_section<FINAL_SECTION & 
       correct_answers<2 & final_exam_in_progress=0 & answers_submitted=0 ->
        0.7:(correct_answers'=correct_answers+1) + 0.3:(correct_answers'=correct_answers);
    
    // Section completion (only when answers are correct)
    [] enrolled=1 & current_section<MAX_SECTIONS & correct_answers=2 & 
       final_exam_in_progress=0 & answers_submitted=0 ->
        (current_section'=current_section+1) & (correct_answers'=0) & 
        (progress_saved'=1) & (previous_section'=current_section);
    
    // Final exam (only when all sections complete)
    [] enrolled=1 & current_section=FINAL_SECTION & final_exam_in_progress=1 & 
       final_points<MIN_POINTS_TO_PASS & answers_submitted=0 ->
        0.7:(final_points'=final_points+1) + 0.3:(final_points'=final_points);
    
    // Answer submission (only during final exam)
    [] enrolled=1 & final_exam_in_progress=1 & answers_submitted=0 & 
       current_section=FINAL_SECTION ->
        (answers_submitted'=1);
    
    // Course creation - MODIFIED
    [] auth=1 & course_created=0 -> (course_created'=1);
    [] course_created=1 & has_sections=0 -> (has_sections'=1);
    
endmodule

// Labels for properties
label "enrolled_twice" = enrolled=1 & previous_section>0;
label "unauthenticated_enrolled" = enrolled=1 & auth=0;
label "unauthorized_access" = enrolled=0 & current_section>0;
label "section_skipped" = current_section>previous_section+1;
label "invalid_pass" = current_section=FINAL_SECTION & final_points<MIN_POINTS_TO_PASS;
label "invalid_section_completion" = current_section>0 & current_section<MAX_SECTIONS & 
    correct_answers<2 & progress_saved=1;
label "early_final" = current_section<MAX_SECTIONS & final_exam_in_progress=1;
label "progress_while_logged_out" = auth=0 & (correct_answers>0 | final_exam_in_progress=1);
label "answer_modified" = answers_submitted=1 & final_exam_in_progress=0;
label "section_progress_saved" = correct_answers=2 & current_section<MAX_SECTIONS;
label "early_results" = final_exam_in_progress=1 & answers_submitted=0 & final_points>0;
label "empty_course_enrolled" = has_sections=0 & enrolled=1;

label "teacher_creating_course" = course_created=1 & auth=0;
label "adding_section_before_course" = has_sections=1 & course_created=0;
