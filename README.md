# The Salon Members

An in-development program that automatically does Memrise learning sessions for you. Once complete, it will get you the target you need swiftly and efficiently. 

Memrise is a British language-learning platform that uses spaced repetition (a similar concept to flashcards) to increase the rate of learning, and is by far, in my opinion, one of the easiest ways to learn a new language. Give it a try!

This program can be considered a tribute to my GCSE Spanish class from eons ago, and the Memrise 'lab' lessons that we all very much enjoyed.

---

**Important message** - use this ethically. Memrise is there to teach you a new language - whether it be for a subject or a hobby, at the end of the day, the only person you're cheating is _yourself_.

---

## Usage

1. Download the zip folder or clone via Git or GitHub CLI.

```bash
git clone https://github.com/mjsandagi/the-salon-members.git
```

```bash
gh repo clone mjsandagi/the-salon-members
```

2. Install the required dependencies

```bash
pip install -r requirements.txt
```

3. Make sure you are happy for Microsoft Edge to be used as your browser. If not, see line 69 in `app.py`, which has comments with further instructions.

4. Run the program

```
python app.py
```

-   It will ask you to enter your Memrise details (securely), and provide some additional information.

```
--------------------------------------------------------
Welcome to Salon Members. (Selenium - Memrise? Get it?)
--------------------------------------------------------
<insert information (just run the program and you'll see it)>
--------------------------------------------------------
Enter your Memrise username (with email):
Enter your Memrise password:
--------------------------------------------------------
```

5. The program will then open up an instance of your browser, with a banner saying `<browser> is being controlled by automated testing software`.
   Sit back and relax. You can use your computer as normal, but don't close the browser window.

## How it works (the "idea")

1. **User Details**: The script prompts for your Memrise username and password, securely handling input with `getpass()`.

2. **WebDriver**: It launches a Selenium WebDriver (`webdriver.Edge()`, modifiable for other browsers) to automate Memrise.

3. **Login**: The bot fills in the login form and submits it using the provided credentials.

4. **Lesson Selection**: It navigates to the lesson section, selecting a new lesson or learning activity.

5. **Word Retrieval**: During the session, it extracts and stores word pairs (target and native language) in a dictionary.

6. **Execution**: After login, the bot automates lesson interaction and exits once the session is complete.


## Furina's Salon Members

![Furina's salon](https://upload-os-bbs.hoyolab.com/upload/2023/11/12/19200721/d5d9f487481ddb92dea2e0910ae75c63_237950955455513173.png)

Source: HoyoLab [@Kyuuyuuno](https://www.hoyolab.com/article/23112995)
