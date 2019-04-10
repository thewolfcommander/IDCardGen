from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.conf import settings

UPLOAD_DIRECTORY_PROFILEPHOTO = 'images_profilephoto'
UPLOAD_DIRECTORY_ID_CARD_PHOTO = 'images_idcardphoto'

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to handle all the operations for the Custom User model
    """
    def create_user(self, user_id, mobile_number, email, password, **extra_fields):

        user = self.model(user_id=user_id, mobile_number=mobile_number, email=email, *extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, mobile_number, email, password, **extra_fields):
        user = self.create_user(user_id, mobile_number, email, password, **extra_fields)
        user.is_admin=True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(user_id=username)

class User(AbstractBaseUser, PermissionsMixin):
    """
    User that is capable of using the Information System
    """
    GENDER = [
        ('MALE', "MALE"),
        ('FEMALE', "FEMALE"),
        ('TRANSGENDER', "TRANSGENDER"),
        ('PREFER_NOT_TO_SAY', "PREFER_NOT_TO_SAY")
    ]

    upload_directory = 'user_images'

    user_id = models.CharField(max_length=24, null=True, blank=True, unique=True, help_text="User's unique user id that is always used to login.")
    full_name = models.CharField(max_length=255, null=True, blank=True, help_text="User's full name")
    gender = models.CharField(max_length=255, choices=GENDER, null=True, blank=True, help_text="User's Gender")
    email = models.EmailField(max_length=255, blank=True, null=True, default='', help_text="User's Email")
    mobile_number = models.CharField(max_length=10, blank=True, null=True, help_text="User's Mobile number")
    profile_photo = models.ImageField(max_length=255, blank=True, null=True, upload_to=UPLOAD_DIRECTORY_PROFILEPHOTO, help_text="User's Profile photo")

    is_admin = models.BooleanField(default=False)
    is_executive = models.BooleanField(default=False)
    is_photographer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['mobile_number', 'email',]
    UNIQUE_TOGETHER = ['user_id', 'email']

    def __str__(self):
        return '%s - %s'%(self.id, self.full_name)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class StudentInformation(models.Model):
    """
    Student Information being uploaded by the Executive
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, help_text="User Relationship with this model.")
    full_name = models.CharField(max_length=255, null=True, blank=True, help_text="Student's full name")
    father_name = models.CharField(max_length=255, null=True, blank=True, help_text="Father's name of student.")
    mother_name = models.CharField(max_length=255, null=True, blank=True, help_text="Mother's name of student.")
    studying_class = models.CharField(max_length=10, null=True, blank=True, help_text="Class in which student is currently studying.")
    section = models.CharField(max_length=10, null=True, blank=True, help_text="Section of class in which student is currently studying.")
    id_card_photo = models.ImageField(max_length=255, upload_to=UPLOAD_DIRECTORY_ID_CARD_PHOTO, null=True, blank=True, help_text="Student's ID card photo that has been uploaded by Photographer.")
    school_name = models.CharField(max_length=255, null=True, blank=True, help_text="Student's school name.")
    school_address_full = models.CharField(max_length=524, null=True, blank=True, help_text="Student's School complete address.")
    mobile_number = models.CharField(max_length=20, null=True, blank=True, help_text="Student's mobile number.")
    email = models.CharField(max_length=255, null=True, blank=True, help_text="Student's email id.")

    class Meta:
        unique_together = ['user', 'full_name', 'father_name', 'email']

class SchoolInformation(models.Model):
    """
    School Information Complete
    """
    school_code = models.CharField(max_length=255, null=True,blank=True, help_text="School Code by which it is unique")
    school_name = models.CharField(max_length=255, null=True,blank=True, help_text="School Name full")
    school_address_line1 = models.CharField(max_length=255, null=True,blank=True, help_text="School address line 1")
    school_address_line2 = models.CharField(max_length=255, null=True,blank=True, help_text="School Address line 2")
    school_city = models.CharField(max_length=255, null=True,blank=True, help_text="School City in which it is located.")
    school_state = models.CharField(max_length=255, null=True,blank=True, help_text="School state in which it is located.")
    zipcode = models.CharField(max_length=255, null=True,blank=True, help_text="School Area's pincode.")
    school_principal_name = models.CharField(max_length=255, null=True,blank=True, help_text="School's prinicipal name.")

    def __str__(self):
        return "%s - %s, %s, %s, %s, %s"%(self.school_code, self.school_name, self.school_address_line1, self.school_address_line2, self.school_city, self.school_state)

class Feedback(models.Model):
    email = models.CharField(max_length=255, null=True, blank=True, help_text="Email of the person who is giving feedback on the system.")
    name = models.CharField(max_length=255, null=True, blank=True, help_text="Name of the person who is giving feedback on the system.")
    message = models.CharField(max_length=1055, null=True, blank=True, help_text="Message of the person who is giving feedback on the system.")

class VerificationCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, help_text="User model Relationship")
    student_information = models.ForeignKey(StudentInformation, on_delete=models.DO_NOTHING, help_text="Student Information model Relationship")
    is_verified_by_student = models.BooleanField(default=False)