import boto3

ses =boto3.client('ses', region_name='eu-north-1')
response=ses.list_verified_email_addresses()
print(response)


#Create Template for Email
def createtemplate():
 response2 = ses.create_template(
    Template={
        'TemplateName': 'string3',
        'SubjectPart': 'string3',
        'TextPart': 'string3',
        'HtmlPart': 'string3'
    })
 print(response2)


#Listing ALl Templates
def list_templates():
 response=ses.list_templates()
 print(response)



#Send Email Function
def sendemail():

#Sending Email
 response22=ses.send_email(
    Source='as1987137@gmail.com',
    Destination={
        'ToAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
        'CcAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
    },
    Message={
        'Subject': {
            'Data': 'Hello Brother',
            'Charset': 'utf-8'
        },
        'Body': {
            'Text': {
                'Data': 'Hi, Consider My Message ',
                'Charset': 'utf-8'
            }
        }
    })


#Update Template
def update_template():
 template_name = 'string3'

 updated_subject = 'Testing Email'
 updated_text_body = 'This is the updated text body of the email.'


 response2 = ses.update_template(
    Template={
        'TemplateName': template_name,
        'SubjectPart': updated_subject,
        'TextPart': updated_text_body,

    })
 print(response2)


#Send Email with TemplateSend a message

def sendtemplatedemail():
 template_name = 'string3'
 response = ses.send_templated_email(
    Source='as1987137@gmail.com',
    Destination={
        'ToAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
        'CcAddresses': [
            'msami.bese22seecs@seecs.edu.pk',
        ],
    },
    Template=template_name,  # Use the template name
    TemplateData='{}',  # You can provide template data if your template expects variables
      )
 print(response)