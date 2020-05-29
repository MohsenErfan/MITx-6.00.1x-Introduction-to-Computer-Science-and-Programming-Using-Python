def decrypt_story():
    cipher_story = CiphertextMessage(get_story_string())
    return cipher_story.decrypt_message()
