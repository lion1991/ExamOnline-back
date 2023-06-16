from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('user', auto_views.UserViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('department', auto_views.DepartmentViewSet)
    
router.register('teacher', auto_views.TeacherViewSet)
    
router.register('student', auto_views.StudentViewSet)
    
router.register('user_roles_info', auto_views.UserRolesInfoViewSet)
    
router.register('paper', auto_views.PaperViewSet)
    
router.register('exam', auto_views.ExamViewSet)
    
router.register('grade', auto_views.GradeViewSet)
    
router.register('practice', auto_views.PracticeViewSet)
    
router.register('choice', auto_views.ChoiceViewSet)
    
router.register('choice_mu', auto_views.ChoiceMuViewSet)
    
router.register('fill', auto_views.FillViewSet)
    
router.register('judge', auto_views.JudgeViewSet)
    
router.register('program', auto_views.ProgramViewSet)
    
router.register('choice_record', auto_views.ChoiceRecordViewSet)
    
router.register('choice_mu_record', auto_views.ChoiceMuRecordViewSet)
    
router.register('fill_record', auto_views.FillRecordViewSet)
    
router.register('judge_record', auto_views.JudgeRecordViewSet)
    
router.register('program_record', auto_views.ProgramRecordViewSet)
    
router.register('limit_file', auto_views.LimitFileViewSet)
    
router.register('random_file_id', auto_views.RandomFileIdViewSet)
    
router.register('files', auto_views.FilesViewSet)
    
router.register('personal_grade_files', auto_views.PersonalGradeFilesViewSet)
    
router.register('captain_files', auto_views.CaptainFilesViewSet)
    
router.register('exam_files', auto_views.ExamFilesViewSet)
    
router.register('judge_files', auto_views.JudgeFilesViewSet)
    
router.register('subject', auto_views.SubjectViewSet)
    
router.register('score', auto_views.ScoreViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    