from django.db import models

# Create your models here.

class Bulb(models.Model) :
    location=models.CharField(max_length=225)
    def __str__(self):
        return f"{self.id}-{self.location}"

class IssueBase(models.Model) :
    bulb=models.ForeignKey("website.Bulb",on_delete= models.CASCADE)
    class Meta :
        abstract=True

class CommonIssue(IssueBase) :
    def __str__(self):
        return f"ST-{self.bulb.id}" 

class CurrentLeakeageIssue(IssueBase) :
    def __str__(self):
        return f"ST-{self.bulb.id}" 
    
class BrokenWireIssue(IssueBase) :
    def __str__(self):
        return f"ST-{self.bulb.id}" 
    
class NoSignalIssue(IssueBase) :
    def __str__(self):
        return f"ST-{self.bulb.id}" 
    
ALL_ISSUES_MODELS=[
    CommonIssue,
    CurrentLeakeageIssue,
    BrokenWireIssue,
    NoSignalIssue,
]