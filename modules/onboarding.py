import os
import json

class OnboardingWizard:
    def __init__(self, profile_path="profile.json"):
        self.profile_path = profile_path

    def profile_exists(self):
        return os.path.exists(self.profile_path)

    def load_profile(self):
        with open(self.profile_path, 'r') as f:
            return json.load(f)

    def start_wizard(self):
        """
        Interactive console wizard to set up the companion.
        In a real bot, this would happen via chat messages.
        """
        print("\n" + "="*40)
        print(" WELCOME TO OPENCLAW COMPANION SETUP")
        print("="*40)
        print("It seems you are new here. Let's create your partner.\n")

        # Step 1: Visuals
        print("1. [VISUALS] Please provide the path to a reference photo (e.g., C:/photos/girl.jpg):")
        ref_photo = input(">> ").strip()
        
        # Step 2: Voice
        print("\n2. [VOICE] Please provide the path to a voice sample (wav/mp3):")
        voice_sample = input(">> ").strip()

        # Step 3: Personality
        print("\n3. [PERSONALITY] Describe her character (e.g., 'Sarcastic goth girl who loves gaming'):")
        personality = input(">> ").strip()

        profile_data = {
            "reference_photo": ref_photo,
            "voice_sample": voice_sample,
            "personality_prompt": personality,
            "nsfw_enabled": True 
        }

        with open(self.profile_path, 'w') as f:
            json.dump(profile_data, f, indent=4)
        
        print("\n[+] Setup Complete! Switching to Chat Mode...")
        return profile_data
