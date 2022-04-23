from os import link
from pyexpat import model
from statistics import mode
from xmlrpc.client import Boolean
from django.db import models

# Create your models here.
from django.db import models



class Website(models.Model):

    link = models.TextField()

    UsingIP = models.BooleanField()

    LongURL = models.BooleanField()

    Symbol = models.BooleanField()

    Redirecting = models.BooleanField()

    PrefixSuffix = models.BooleanField()

    SubDomains = models.IntegerField()

    HTTPS = models.IntegerField()

    DomainRegLen = models.BooleanField()

    Favicon = models.BooleanField()

    NonStdPort = models.BooleanField()

    HTTPSDomainURL = models.BooleanField()

    RequestURL = models.BooleanField()

    AnchorURL = models.IntegerField()

    LinksInScriptTags = models.IntegerField()

    ServerFormHandler = models.BooleanField()

    InfoEmail = models.BooleanField()

    AbnormalURL = models.BooleanField()

    WebsiteForwarding = models.BooleanField()

    DNSRecording = models.BooleanField()

    PageRank = models.BooleanField()