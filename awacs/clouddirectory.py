# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Cloud Directory'
prefix = 'clouddirectory'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddFacetToObject = Action('AddFacetToObject')
ApplySchema = Action('ApplySchema')
AttachObject = Action('AttachObject')
AttachPolicy = Action('AttachPolicy')
AttachToIndex = Action('AttachToIndex')
BatchRead = Action('BatchRead')
BatchWrite = Action('BatchWrite')
CreateDirectory = Action('CreateDirectory')
CreateFacet = Action('CreateFacet')
CreateIndex = Action('CreateIndex')
CreateObject = Action('CreateObject')
CreateSchema = Action('CreateSchema')
DeleteDirectory = Action('DeleteDirectory')
DeleteFacet = Action('DeleteFacet')
DeleteObject = Action('DeleteObject')
DeleteSchema = Action('DeleteSchema')
DetachFromIndex = Action('DetachFromIndex')
DetachObject = Action('DetachObject')
DetachPolicy = Action('DetachPolicy')
DisableDirectory = Action('DisableDirectory')
EnableDirectory = Action('EnableDirectory')
GetDirectory = Action('GetDirectory')
GetFacet = Action('GetFacet')
GetObjectInformation = Action('GetObjectInformation')
GetSchemaAsJson = Action('GetSchemaAsJson')
ListAppliedSchemaArns = Action('ListAppliedSchemaArns')
ListAttachedIndices = Action('ListAttachedIndices')
ListDevelopmentSchemaArns = Action('ListDevelopmentSchemaArns')
ListDirectories = Action('ListDirectories')
ListFacetAttributes = Action('ListFacetAttributes')
ListFacetNames = Action('ListFacetNames')
ListIndex = Action('ListIndex')
ListObjectAttributes = Action('ListObjectAttributes')
ListObjectChildren = Action('ListObjectChildren')
ListObjectParents = Action('ListObjectParents')
ListObjectPolicies = Action('ListObjectPolicies')
ListPolicyAttachments = Action('ListPolicyAttachments')
ListPublishedSchemaArns = Action('ListPublishedSchemaArns')
ListTagsForResource = Action('ListTagsForResource')
LookupPolicy = Action('LookupPolicy')
PublishSchema = Action('PublishSchema')
PutSchemaFromJson = Action('PutSchemaFromJson')
RemoveFacetFromObject = Action('RemoveFacetFromObject')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateFacet = Action('UpdateFacet')
UpdateObjectAttributes = Action('UpdateObjectAttributes')
UpdateSchema = Action('UpdateSchema')
