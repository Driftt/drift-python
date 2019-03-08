[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![PyPI version](https://badge.fury.io/py/drift-python.svg)](https://badge.fury.io/py/drift-python)

<p align="center">
    <img src="img/drift_python.png" width="300"/>
</p>

# Drift Python
A [Drift API](https://devdocs.drift.com) wrapper written in Python.


## Getting Started
To get started run `pip install drift-python`

```python
from drift import Drift
drift = Drift("YOUR ACCESS TOKEN")
```

## Contacts
Read the docs here: [Contacts API](https://devdocs.drift.com/docs/contact-model).

**Available Methods**

- `drift.contacts.get()`
    - contact_id (required)
    - email (optional)
    - limit (optional)
    - 
- `drift.contacts.create()`
    - **attributes (required)
    
    Example:
    `drift.contacts.create(email='johndoe@drift.com')` 
    
- `drift.contacts.update()`
    - contact_id (required)
    - **attributes (required)

- `drift.contacts.delete()`
    - contact_id (required)
    
- `drift.contacts.add_tags()`
    - contact_id (required)
    - tags (required)
    
    Example:
    ```
    drift.contacts.add_tags(
      conversation_id=1, 
      tags=[{'name': 'My Tag'}]
    )
    ```
    
- `drift.contacts.remove_tag()`
    - contact_id (required)
    - tag_name (required)
    
- `drift.contacts.remove_tags_bulk()`
    - contact_id (required)

## Conversations
Read the docs here [Conversations API](https://devdocs.drift.com/docs/conversation-overview)

**Available Methods**

- `drift.conversations.get()`
    - conversation_id (required)
    
- `drift.conversations.list()`
    - limit (optional) - defaults to `50`
    - next_ (optional)

- `drift.conversations.create_message()`
    - conversation_id (required)
    - org_id (required)
    - type (required)
    - body (optional)
    - buttons (optional)
    - edited_message_id (optional)
    - edit_type (optional)
    
    Example:
    ```
    drift.conversations.create_message(
        conversation_id=1,
        org_id=1,
        type='chat'
    )
    ```
    
- `drift.conversations.get_messages()`
    - conversation_id (required)
    - next_ (optional)

- `drift.conversations.get_attachments()`
    - doc_id (required)
    
- `drift.conversations.get_metrics()`
    - query (required)
    
    Example:
    ```
    drift.conversations.get_metrics(
        {
          "metrics": [
            {
              "type": "AVG",
              "property": "numBotMessages"
            }
          ],
          "filters": [
            {
              "property": "createdAt",
              "operation": "BETWEEN",
              "values": ["2018-01-01", "2018-07-31"]
            }
          ]
        }
    )
  
    ```

## Users
Read the docs here [Users API](https://devdocs.drift.com/docs/user-model)

**Available Methods**

- `drift.users.get()`
    - user_id (required)
    
- `drift.users.list()`

- `drift.users.update()`
    - user_id (required)
    - **attributes (required)

    Example:
    drift.users.update(243266, phone='555-555-5555')
    
 
## Contributors
- Lemuel Boyce [rhymiz](https://github.com/rhymiz)
- Chris Buonocore [cbonoz](https://github.com/cbonoz)


## Support / Feedback / Bugs
For support and feedback, you can find us on [Slack](https://join.slack.com/t/devdrift/shared_invite/enQtMzg4MTI3NDk5NDQ0LWUwMWYzZTkyMmQ1YjdkNjkwZDg2Mzk2YjAyMDg4MWViYmIzZjVhZTczNDQwMDVjOGRjZGU5OTkxMWQ0ZGU0Mjg)!

If you've found a bug, feel free to open up a PR with a fix or submit an issue. Let us know in the dev slack!
