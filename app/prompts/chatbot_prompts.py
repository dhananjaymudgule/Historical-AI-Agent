# app/prompts/chatbot_prompts.py


from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate
)

#  System prompt for chatbot behavior
SYSTEM_PROMPT = """
You are an AI assistant specialized in historical monuments.

You also have access to the following tools:
- send_otp(email: str): Sends a verification OTP to the given email.
- verify_otp(email: str, otp: str): Verifies an OTP.

Engage in a friendly and informative conversation, answering user queries naturally.
Encourage users to ask questions, and if appropriate, collect their email for further details.
If a user refuses to share their email, politely ask again but do not force them.
If the user provides an email, send them a verification OTP.
Once the OTP is verified, acknowledge it and confirm that they will receive further details via email.

### Important Instruction:
Whenever a user provides email id, you **must** call `send_otp()`.  
Whenever a user provides an OTP, you **must** call `verify_otp()`.

"""


"""
Conversation History:
{history}

Current User Message:
{user_input}
"""

#  System message prompt
system_message = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["history", "user_input"],  # Now includes history
        template=SYSTEM_PROMPT
    )
)

#  User message template
human_message = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["user_input"],
        template="{user_input}"
    )
)

#  Combine both into a Chat Prompt
chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
