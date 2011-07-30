# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

## IMPORTANT! I removed all id = IntegerField() so that the default id = IntegerField(primary_key=True) was used
## --Issac
## Also needed to change to positive max_length on a couple of char fields
## So ForeignKeys are all in as IntegerFields..that's a bit of a pain

from django.db import models

class Annotation(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    text = models.TextField()
    changelog = models.CharField(max_length=255)
    created = models.DateTimeField()
    
    class Meta:
        db_table = u'annotation'

class Artist(models.Model):
    gid = models.TextField(blank=True, null=True) # This field type is a guess.
    name = models.ForeignKey("ArtistName", db_column="name")
    sort_name = models.IntegerField(blank=True, null=True)
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    type = models.ForeignKey("ArtistType", db_column="type")
    country = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    ipi_code = models.CharField(max_length=11, blank=True, null=True)
    edits_pending = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        if self.name:
            return u"%s - %s" % (self.id, self.name.name)
        else:
            return u"%s" % self.id
    
    class Meta:
        db_table = u'artist'

class ArtistAlias(models.Model):
    artist = models.ForeignKey("Artist", db_column="artist")
    name = models.ForeignKey("ArtistName")
    locale = models.TextField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'artist_alias'

class ArtistAnnotation(models.Model):
    artist = models.ForeignKey("Artist", db_column="artist")
    annotation = models.IntegerField()
    class Meta:
        db_table = u'artist_annotation'

class ArtistMeta(models.Model):
    rating = models.SmallIntegerField()
    rating_count = models.IntegerField()
    class Meta:
        db_table = u'artist_meta'

class ArtistTag(models.Model):
    artist = models.ForeignKey("Artist", db_column="artist")
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'artist_tag'

class ArtistRatingRaw(models.Model):
    artist = models.ForeignKey("Artist", db_column="artist")
    editor = models.ForeignKey("Editor", db_column="editor")
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'artist_rating_raw'

class ArtistTagRaw(models.Model):
    artist = models.ForeignKey("Artist", db_column="artist")
    editor = models.ForeignKey("Editor", db_column="editor")
    tag = models.IntegerField()
    class Meta:
        db_table = u'artist_tag_raw'

class ArtistCredit(models.Model):
    name = models.ForeignKey("ArtistName")
    artist_count = models.SmallIntegerField()
    ref_count = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'artist_credit'

class ArtistCreditName(models.Model):
    artist_credit = models.ForeignKey("ArtistCredit", db_column="artist_credit")
    position = models.SmallIntegerField()
    artist = models.ForeignKey("Artist", db_column="artist")
    name = models.ForeignKey("ArtistName")
    join_phrase = models.TextField()
    class Meta:
        db_table = u'artist_credit_name'

class ArtistGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'artist_gid_redirect'

class ArtistName(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        db_table = u'artist_name'

class ArtistType(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'artist_type'

class Cdtoc(models.Model):
    discid = models.TextField() # This field type is a guess.
    freedb_id = models.TextField() # This field type is a guess.
    track_count = models.IntegerField()
    leadout_offset = models.IntegerField()
    track_offset = models.TextField() # This field type is a guess.
    degraded = models.BooleanField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'cdtoc'

class CdtocRaw(models.Model):
    release = models.ForeignKey("Release", db_column="release")
    discid = models.TextField() # This field type is a guess.
    track_count = models.IntegerField()
    leadout_offset = models.IntegerField()
    track_offset = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'cdtoc_raw'

class Clientversion(models.Model):
    version = models.CharField(max_length=64)
    created = models.DateTimeField()
    class Meta:
        db_table = u'clientversion'

class Country(models.Model):
    iso_code = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'country'

class Edit(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    data = models.TextField()
    yes_votes = models.IntegerField()
    no_votes = models.IntegerField()
    autoedit = models.SmallIntegerField()
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()
    expire_time = models.DateTimeField()
    language = models.IntegerField()
    quality = models.SmallIntegerField()
    class Meta:
        db_table = u'edit'

class EditNote(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    edit = models.ForeignKey("Edit")
    text = models.TextField()
    post_time = models.DateTimeField()
    class Meta:
        db_table = u'edit_note'

class EditArtist(models.Model):
    edit = models.ForeignKey("Edit")
    artist = models.ForeignKey("Artist", db_column="artist")
    status = models.SmallIntegerField()
    class Meta:
        db_table = u'edit_artist'

class EditLabel(models.Model):
    edit = models.ForeignKey("Edit")
    label = models.ForeignKey("Label")
    status = models.SmallIntegerField()
    class Meta:
        db_table = u'edit_label'

class EditRelease(models.Model):
    edit = models.ForeignKey("Edit")
    release = models.ForeignKey("Release", db_column="release")
    class Meta:
        db_table = u'edit_release'

class EditReleaseGroup(models.Model):
    edit = models.ForeignKey("Edit")
    release_group = models.IntegerField()
    class Meta:
        db_table = u'edit_release_group'

class EditRecording(models.Model):
    edit = models.ForeignKey("Edit")
    recording = models.ForeignKey("Recording")
    class Meta:
        db_table = u'edit_recording'

class EditWork(models.Model):
    edit = models.ForeignKey("Edit")
    work = models.ForeignKey("Work", db_column="work")
    class Meta:
        db_table = u'edit_work'

class EditUrl(models.Model):
    edit = models.ForeignKey("Edit")
    url = models.IntegerField()
    class Meta:
        db_table = u'edit_url'

class Editor(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    privs = models.IntegerField()
    email = models.CharField(max_length=64)
    website = models.CharField(max_length=255)
    bio = models.TextField()
    member_since = models.DateTimeField()
    email_confirm_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    edits_accepted = models.IntegerField()
    edits_rejected = models.IntegerField()
    auto_edits_accepted = models.IntegerField()
    edits_failed = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'editor'

class EditorPreference(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    class Meta:
        db_table = u'editor_preference'

class EditorSubscribeArtist(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    artist = models.ForeignKey("Artist", db_column="artist")
    last_edit_sent = models.IntegerField()
    deleted_by_edit = models.IntegerField()
    merged_by_edit = models.IntegerField()
    class Meta:
        db_table = u'editor_subscribe_artist'

class EditorSubscribeLabel(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    label = models.ForeignKey("Label")
    last_edit_sent = models.IntegerField()
    deleted_by_edit = models.IntegerField()
    merged_by_edit = models.IntegerField()
    class Meta:
        db_table = u'editor_subscribe_label'

class EditorSubscribeEditor(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    subscribed_editor = models.IntegerField()
    last_edit_sent = models.IntegerField()
    class Meta:
        db_table = u'editor_subscribe_editor'

class Gender(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'gender'

class Isrc(models.Model):
    recording = models.ForeignKey("Recording")
    isrc = models.TextField() # This field type is a guess.
    source = models.SmallIntegerField()
    edits_pending = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'isrc'

class LArtistArtist(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_artist'

class LArtistLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_label'

class LArtistRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_recording'

class LArtistRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_release'

class LArtistReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_release_group'

class LArtistUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_url'

class LArtistWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_artist_work'

class LLabelLabel(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_label_label'

class LLabelRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_label_recording'

class LLabelRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_label_release'

class LLabelReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_label_release_group'

class LLabelUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_label_url'

class LLabelWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_label_work'

class LRecordingRecording(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_recording_recording'

class LRecordingRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_recording_release'

class LRecordingReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_recording_release_group'

class LRecordingUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_recording_url'

class LRecordingWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_recording_work'

class LReleaseRelease(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_release'

class LReleaseReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_release_group'

class LReleaseUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_url'

class LReleaseWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_work'

class LReleaseGroupReleaseGroup(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_group_release_group'

class LReleaseGroupUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_group_url'

class LReleaseGroupWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_release_group_work'

class LUrlUrl(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_url_url'

class LUrlWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_url_work'

class LWorkWork(models.Model):
    link = models.IntegerField()
    entity0 = models.IntegerField()
    entity1 = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'l_work_work'

class Label(models.Model):
    gid = models.TextField() # This field type is a guess.
    name = models.IntegerField()
    sort_name = models.IntegerField()
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    label_code = models.IntegerField()
    type = models.IntegerField()
    country = models.IntegerField()
    comment = models.CharField(max_length=255)
    ipi_code = models.CharField(max_length=11)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'label'

class LabelRatingRaw(models.Model):
    label = models.ForeignKey("Label")
    editor = models.ForeignKey("Editor", db_column="editor")
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'label_rating_raw'

class LabelTagRaw(models.Model):
    label = models.ForeignKey("Label")
    editor = models.ForeignKey("Editor", db_column="editor")
    tag = models.IntegerField()
    class Meta:
        db_table = u'label_tag_raw'

class LabelAlias(models.Model):
    label = models.ForeignKey("Label")
    name = models.IntegerField()
    locale = models.TextField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'label_alias'

class LabelAnnotation(models.Model):
    label = models.ForeignKey("Label")
    annotation = models.IntegerField()
    class Meta:
        db_table = u'label_annotation'

class LabelMeta(models.Model):
    rating = models.SmallIntegerField()
    rating_count = models.IntegerField()
    class Meta:
        db_table = u'label_meta'

class LabelGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'label_gid_redirect'

class LabelName(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        db_table = u'label_name'

class LabelTag(models.Model):
    label = models.ForeignKey("Label")
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'label_tag'

class LabelType(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'label_type'

class Language(models.Model):
    iso_code_3t = models.TextField() # This field type is a guess.
    iso_code_3b = models.TextField() # This field type is a guess.
    iso_code_2 = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    class Meta:
        db_table = u'language'

class Link(models.Model):
    link_type = models.IntegerField()
    begin_date_year = models.SmallIntegerField(blank=True, null=True)
    begin_date_month = models.SmallIntegerField(blank=True, null=True)
    begin_date_day = models.SmallIntegerField(blank=True, null=True)
    end_date_year = models.SmallIntegerField(blank=True, null=True)
    end_date_month = models.SmallIntegerField(blank=True, null=True)
    end_date_day = models.SmallIntegerField(blank=True, null=True)
    attribute_count = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'link'

class LinkAttribute(models.Model):
    link = models.IntegerField()
    attribute_type = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'link_attribute'

class LinkAttributeType(models.Model):
    parent = models.IntegerField()
    root = models.IntegerField()
    child_order = models.IntegerField()
    gid = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=255)
    description = models.TextField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'link_attribute_type'

class LinkType(models.Model):
    parent = models.IntegerField()
    child_order = models.IntegerField()
    gid = models.TextField() # This field type is a guess.
    entity_type0 = models.CharField(max_length=50)
    entity_type1 = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField()
    link_phrase = models.CharField(max_length=255)
    reverse_link_phrase = models.CharField(max_length=255)
    short_link_phrase = models.CharField(max_length=255)
    priority = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'link_type'

class LinkTypeAttributeType(models.Model):
    link_type = models.IntegerField()
    attribute_type = models.IntegerField()
    min = models.SmallIntegerField()
    max = models.SmallIntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'link_type_attribute_type'

class EditorCollection(models.Model):
    gid = models.TextField() # This field type is a guess.
    editor = models.ForeignKey("Editor", db_column="editor")
    name = models.CharField(max_length=128)
    public = models.BooleanField()
    class Meta:
        db_table = u'editor_collection'

class EditorCollectionRelease(models.Model):
    collection = models.IntegerField()
    release = models.ForeignKey("Release", db_column="release")
    class Meta:
        db_table = u'editor_collection_release'

class EditorWatchPreferences(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    notify_via_email = models.BooleanField()
    notification_timeframe = models.TextField() # This field type is a guess.
    last_checked = models.DateTimeField()
    class Meta:
        db_table = u'editor_watch_preferences'

class EditorWatchArtist(models.Model):
    artist = models.ForeignKey("Artist", db_column="artist")
    editor = models.ForeignKey("Editor", db_column="editor")
    class Meta:
        db_table = u'editor_watch_artist'

class EditorWatchReleaseGroupType(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    release_group_type = models.IntegerField()
    class Meta:
        db_table = u'editor_watch_release_group_type'

class EditorWatchReleaseStatus(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    release_status = models.IntegerField()
    class Meta:
        db_table = u'editor_watch_release_status'

class Medium(models.Model):
    tracklist = models.IntegerField()
    release = models.ForeignKey("Release", db_column="release")
    position = models.IntegerField()
    format = models.IntegerField()
    name = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'medium'

class MediumCdtoc(models.Model):
    medium = models.IntegerField()
    cdtoc = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'medium_cdtoc'

class MediumFormat(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField()
    child_order = models.IntegerField()
    year = models.SmallIntegerField()
    has_discids = models.BooleanField()
    class Meta:
        db_table = u'medium_format'

class Puid(models.Model):
    puid = models.TextField() # This field type is a guess.
    version = models.IntegerField()
    class Meta:
        db_table = u'puid'

class ReplicationControl(models.Model):
    current_schema_sequence = models.IntegerField()
    current_replication_sequence = models.IntegerField()
    last_replication_date = models.DateTimeField()
    class Meta:
        db_table = u'replication_control'

class Recording(models.Model):
    gid = models.TextField() # This field type is a guess.
    name = models.IntegerField()
    artist_credit = models.IntegerField()
    length = models.IntegerField()
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'recording'

class RecordingRatingRaw(models.Model):
    recording = models.ForeignKey("Recording")
    editor = models.ForeignKey("Editor", db_column="editor")
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'recording_rating_raw'

class RecordingTagRaw(models.Model):
    recording = models.ForeignKey("Recording")
    editor = models.ForeignKey("Editor", db_column="editor")
    tag = models.IntegerField()
    class Meta:
        db_table = u'recording_tag_raw'

class RecordingAnnotation(models.Model):
    recording = models.ForeignKey("Recording")
    annotation = models.IntegerField()
    class Meta:
        db_table = u'recording_annotation'

class RecordingMeta(models.Model):
    rating = models.SmallIntegerField()
    rating_count = models.IntegerField()
    class Meta:
        db_table = u'recording_meta'

class RecordingGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'recording_gid_redirect'

class RecordingPuid(models.Model):
    puid = models.IntegerField()
    recording = models.ForeignKey("Recording")
    edits_pending = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'recording_puid'

class RecordingTag(models.Model):
    recording = models.ForeignKey("Recording")
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'recording_tag'

class Release(models.Model):
    gid = models.TextField() # This field type is a guess.
    name = models.IntegerField()
    artist_credit = models.IntegerField()
    release_group = models.IntegerField()
    status = models.IntegerField()
    packaging = models.IntegerField()
    country = models.IntegerField()
    language = models.IntegerField()
    script = models.IntegerField()
    date_year = models.SmallIntegerField()
    date_month = models.SmallIntegerField()
    date_day = models.SmallIntegerField()
    barcode = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    quality = models.SmallIntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'release'

class ReleaseRaw(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    added = models.DateTimeField()
    last_modified = models.DateTimeField()
    lookup_count = models.IntegerField()
    modify_count = models.IntegerField()
    source = models.IntegerField()
    barcode = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    class Meta:
        db_table = u'release_raw'

class ReleaseTagRaw(models.Model):
    release = models.ForeignKey("Release", db_column="release")
    editor = models.ForeignKey("Editor", db_column="editor")
    tag = models.IntegerField()
    class Meta:
        db_table = u'release_tag_raw'

class ReleaseAnnotation(models.Model):
    release = models.ForeignKey("Release", db_column="release")
    annotation = models.IntegerField()
    class Meta:
        db_table = u'release_annotation'

class ReleaseGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'release_gid_redirect'

class ReleaseMeta(models.Model):
    date_added = models.DateTimeField()
    info_url = models.CharField(max_length=255)
    amazon_asin = models.CharField(max_length=10)
    amazon_store = models.CharField(max_length=20)
    class Meta:
        db_table = u'release_meta'

class ReleaseCoverart(models.Model):
    last_updated = models.DateTimeField()
    cover_art_url = models.CharField(max_length=255)
    class Meta:
        db_table = u'release_coverart'

class ReleaseLabel(models.Model):
    release = models.ForeignKey("Release", db_column="release")
    label = models.ForeignKey("Label")
    catalog_number = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'release_label'

class ReleasePackaging(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'release_packaging'

class ReleaseStatus(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'release_status'

class ReleaseTag(models.Model):
    release = models.ForeignKey("Release", db_column="release")
    tag = models.ForeignKey("Tag")
    count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'release_tag'

class ReleaseGroup(models.Model):
    gid = models.TextField() # This field type is a guess.
    name = models.IntegerField()
    artist_credit = models.IntegerField()
    type = models.IntegerField()
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'release_group'

class ReleaseGroupRatingRaw(models.Model):
    release_group = models.ForeignKey("ReleaseGroup")
    editor = models.ForeignKey("Editor", db_column="editor")
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'release_group_rating_raw'

class ReleaseGroupTagRaw(models.Model):
    release_group = models.IntegerField()
    editor = models.ForeignKey("Editor", db_column="editor")
    tag = models.IntegerField()
    class Meta:
        db_table = u'release_group_tag_raw'

class ReleaseGroupAnnotation(models.Model):
    release_group = models.IntegerField()
    annotation = models.IntegerField()
    class Meta:
        db_table = u'release_group_annotation'

class ReleaseGroupGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'release_group_gid_redirect'

class ReleaseGroupMeta(models.Model):
    release_count = models.IntegerField()
    first_release_date_year = models.SmallIntegerField()
    first_release_date_month = models.SmallIntegerField()
    first_release_date_day = models.SmallIntegerField()
    rating = models.SmallIntegerField()
    rating_count = models.IntegerField()
    class Meta:
        db_table = u'release_group_meta'

class ReleaseGroupTag(models.Model):
    release_group = models.IntegerField()
    tag = models.ForeignKey("Tag")
    count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'release_group_tag'

class ReleaseGroupType(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'release_group_type'

class ReleaseName(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        db_table = u'release_name'

class Script(models.Model):
    iso_code = models.TextField() # This field type is a guess.
    iso_number = models.TextField() # This field type is a guess.
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    class Meta:
        db_table = u'script'

class ScriptLanguage(models.Model):
    script = models.IntegerField()
    language = models.IntegerField()
    frequency = models.IntegerField()
    class Meta:
        db_table = u'script_language'

class Statistic(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    date_collected = models.DateField()
    class Meta:
        db_table = u'statistic'

class Tag(models.Model):
    name = models.CharField(max_length=255)
    ref_count = models.IntegerField()
    class Meta:
        db_table = u'tag'

class TagRelation(models.Model):
    tag1 = models.ForeignKey("Tag", related_name="related_tags_1")
    tag2 = models.ForeignKey("Tag", related_name="related_tags_2")
    weight = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'tag_relation'

class Track(models.Model):
    recording = models.ForeignKey("Recording")
    tracklist = models.ForeignKey("Tracklist", db_column="tracklist")
    position = models.IntegerField()
    name = models.ForeignKey("TrackName", db_column="name")
    artist_credit = models.ForeignKey("ArtistCredit", db_column="artist_credit")
    length = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'track'

class TrackRaw(models.Model):
    release = models.ForeignKey("Release", db_column="release")
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    sequence = models.IntegerField()
    class Meta:
        db_table = u'track_raw'

class TrackName(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        db_table = u'track_name'

class Tracklist(models.Model):
    track_count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'tracklist'

class TracklistIndex(models.Model):
    tracklist = models.IntegerField()
    toc = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'tracklist_index'

class Url(models.Model):
    gid = models.TextField() # This field type is a guess.
    url = models.TextField()
    description = models.TextField()
    ref_count = models.IntegerField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'url'

class UrlGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'url_gid_redirect'

class Vote(models.Model):
    editor = models.ForeignKey("Editor", db_column="editor")
    edit = models.ForeignKey("Edit")
    vote = models.SmallIntegerField()
    vote_time = models.DateTimeField()
    superseded = models.BooleanField()
    class Meta:
        db_table = u'vote'

class Work(models.Model):
    gid = models.TextField() # This field type is a guess.
    name = models.ForeignKey("WorkName")
    artist_credit = models.ForeignKey("ArtistCredit", db_column="artist_credit")
    type = models.ForeignKey("WorkType")
    iswc = models.TextField() # This field type is a guess.
    comment = models.CharField(max_length=255)
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'work'

class WorkRatingRaw(models.Model):
    work = models.ForeignKey("Work", db_column="work")
    editor = models.ForeignKey("Editor", db_column="editor")
    rating = models.SmallIntegerField()
    class Meta:
        db_table = u'work_rating_raw'

class WorkTagRaw(models.Model):
    work = models.ForeignKey("Work", db_column="work")
    editor = models.ForeignKey("Editor", db_column="editor")
    tag = models.IntegerField()
    class Meta:
        db_table = u'work_tag_raw'

class WorkAlias(models.Model):
    work = models.ForeignKey("Work", db_column="work")
    name = models.ForeignKey("WorkName")
    locale = models.TextField()
    edits_pending = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'work_alias'

class WorkAnnotation(models.Model):
    work = models.ForeignKey("Work", db_column="work")
    annotation = models.IntegerField()
    class Meta:
        db_table = u'work_annotation'

class WorkGidRedirect(models.Model):
    gid = models.TextField() # This field type is a guess.
    new_id = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'work_gid_redirect'

class WorkMeta(models.Model):
    rating = models.SmallIntegerField()
    rating_count = models.IntegerField()
    class Meta:
        db_table = u'work_meta'

class WorkName(models.Model):
    name = models.CharField(max_length=128)
    class Meta:
        db_table = u'work_name'

class WorkTag(models.Model):
    work = models.ForeignKey("Work", db_column="work")
    tag = models.IntegerField()
    count = models.IntegerField()
    last_updated = models.DateTimeField()
    class Meta:
        db_table = u'work_tag'

class WorkType(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = u'work_type'

