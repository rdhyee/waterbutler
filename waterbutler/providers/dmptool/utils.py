
def get_dmptool_client(token, sandbox=False):

    # return EvernoteClient(token=token, sandbox=sandbox)
    return None


def get_notebooks(client):

    # noteStore = client.get_note_store()
    # return [{'name': notebook.name,
    #          'guid': notebook.guid,
    #          'stack': notebook.stack,
    #          'defaultNotebook': notebook.defaultNotebook} for notebook in noteStore.listNotebooks()]

    return []


# https://dev.evernote.com/doc/reference/NoteStore.html#Fn_NoteStore_getNotebook


def get_notebook(client, nb_guid):

    # noteStore = client.get_note_store()
    # notebook = noteStore.getNotebook(nb_guid)
    # return {'name': notebook.name,
    #          'guid': notebook.guid,
    #          'stack': notebook.stack,
    #          'defaultNotebook': notebook.defaultNotebook}

    return {}


def notes_metadata(client, **input_kw):
    """ """

    for note_md in []:
        yield note_md

    # # http://dev.evernote.com/documentation/reference/NoteStore.html#Fn_NoteStore_findNotesMetadata

    # noteStore = client.get_note_store()

    # # pull out offset and page_size value if supplied
    # offset = input_kw.pop('offset', 0)
    # page_size = input_kw.pop('page_size', 100)

    # # let's update any keywords that are updated
    # # http://dev.evernote.com/documentation/reference/NoteStore.html#Struct_NotesMetadataResultSpec

    # include_kw = {
    #     'includeTitle': False,
    #     'includeContentLength': False,
    #     'includeCreated': False,
    #     'includeUpdated': False,
    #     'includeDeleted': False,
    #     'includeUpdateSequenceNum': False,
    #     'includeNotebookGuid': False,
    #     'includeTagGuids': False,
    #     'includeAttributes': False,
    #     'includeLargestResourceMime': False,
    #     'includeLargestResourceSize': False
    # }

    # include_kw.update([(k, input_kw[k]) for k in set(input_kw.keys()) & set(include_kw.keys())])

    # # keywords aimed at NoteFilter
    # # http://dev.evernote.com/documentation/reference/NoteStore.html#Struct_NoteFilter
    # filter_kw_list = ('order', 'ascending', 'words', 'notebookGuid', 'tagGuids', 'timeZone', 'inactive', 'emphasized')
    # filter_kw = dict([(k, input_kw[k]) for k in set(filter_kw_list) & set(input_kw.keys())])

    # # what possible parameters are aimed at NoteFilter
    # # order	i32		optional
    # # ascending	bool		optional
    # # words	string		optional
    # # notebookGuid	Types.Guid		optional
    # # tagGuids	list<Types.Guid>		optional
    # # timeZone	string		optional
    # # inactive   bool
    # # emphasized string

    # more_nm = True

    # while more_nm:

    #     # grab a page of data
    #     note_meta = noteStore.findNotesMetadata(NoteFilter(**filter_kw), offset, page_size,
    #                                 NotesMetadataResultSpec(**include_kw))

    #     # yield each individually
    #     for nm in note_meta.notes:
    #         yield nm

    #     # grab next page if there is more to grab
    #     if len(note_meta.notes):
    #         offset += len(note_meta.notes)
    #     else:
    #         more_nm = False


# def get_note(client, guid,
#             withContent=False,
#             withResourcesData=False,
#             withResourcesRecognition=False,
#             withResourcesAlternateData=False):

#     # https://dev.evernote.com/doc/reference/NoteStore.html#Fn_NoteStore_getNote
#     noteStore = client.get_note_store()
#     return noteStore.getNote(guid, withContent, withResourcesData,
#                                  withResourcesRecognition, withResourcesAlternateData)


# def timestamp_iso(ts):
#     """
#     ts in ms since 1970
#     """
#     return datetime.datetime.utcfromtimestamp(ts / 1000.).isoformat()