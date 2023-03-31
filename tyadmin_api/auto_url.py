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
    
router.register('score3', auto_views.Score3ViewSet)
    
router.register('linux_score3', auto_views.LinuxScore3ViewSet)
    
router.register('network_score3', auto_views.NetworkScore3ViewSet)
    
router.register('office_score3', auto_views.OfficeScore3ViewSet)
    
router.register('score4', auto_views.Score4ViewSet)
    
router.register('linux_score4', auto_views.LinuxScore4ViewSet)
    
router.register('network_score4', auto_views.NetworkScore4ViewSet)
    
router.register('office_score4', auto_views.OfficeScore4ViewSet)
    
router.register('score5', auto_views.Score5ViewSet)
    
router.register('linux_score5', auto_views.LinuxScore5ViewSet)
    
router.register('network_score5', auto_views.NetworkScore5ViewSet)
    
router.register('office_score5', auto_views.OfficeScore5ViewSet)
    
router.register('score6', auto_views.Score6ViewSet)
    
router.register('linux_score6', auto_views.LinuxScore6ViewSet)
    
router.register('network_score6', auto_views.NetworkScore6ViewSet)
    
router.register('score7', auto_views.Score7ViewSet)
    
router.register('linux_score7', auto_views.LinuxScore7ViewSet)
    
router.register('network_score7', auto_views.NetworkScore7ViewSet)
    
router.register('score8', auto_views.Score8ViewSet)
    
router.register('linux_score8', auto_views.LinuxScore8ViewSet)
    
router.register('network_score8', auto_views.NetworkScore8ViewSet)
    
router.register('score9', auto_views.Score9ViewSet)
    
router.register('linux_score9', auto_views.LinuxScore9ViewSet)
    
router.register('network_score9', auto_views.NetworkScore9ViewSet)
    
router.register('score10', auto_views.Score10ViewSet)
    
router.register('linux_score10', auto_views.LinuxScore10ViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    