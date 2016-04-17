# blogger json parser

# feed.entry[entry]._
#   published
#   updated
#   title
#       __text
#   content
#       __text
#   category
#       _term (where _term != "http://" + anything
#   total (if > 0 then save link._href where _rel==replies

import json
import traceback

import sys

archive = {}

with open('blogger.json', 'r') as file1:
    entries = json.loads(file1.read())['feed']['entry']
    for entry in entries:
        # check if comment
        if 'in-reply-to' in entry:
            comment = {}
            comment['published'] = entry['published']
            comment['updated'] = entry['updated']
            comment['content'] = entry['content']['__text']
            comment['author'] = entry['author']['name']
            if 'comments' in archive[entry['in-reply-to']['_ref']]:
                archive[entry['in-reply-to']['_ref']]['comments'].append(comment)
            else:
                archive[entry['in-reply-to']['_ref']]['comments'] = [comment]
        else:
            new_entry = {}
            if 'title' in entry:
                new_entry['title'] = entry['title']['__text']
            else:
                new_entry['title'] = 'Untitled'
            new_entry['published'] = entry['published']
            new_entry['updated'] = entry['updated']
            tags = []
            if type(entry['category']) is list:
                for tag in entry['category']:
                    if not tag['_term'].startswith('http://'):
                        tags.append(tag['_term'])
            else:
                if not entry['category']['_term'].startswith('http://'):
                    tags.append(tag['_term'])
            new_entry['content'] = entry['content']['__text']
            if entry['id'] not in archive:
                new_entry['comments'] = []
                archive[entry['id']] = new_entry
            else:
                if 'comments' in archive[entry['id']]:
                    new_entry['comments'] = archive[entry['id']]['comments']
                else:
                    new_entry['comments'] = []
                archive[entry['id']] = new_entry

with file('output.json', 'w+') as file2:
    file2.write(json.dumps(archive))
