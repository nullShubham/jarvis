## What Can This assistant do ?
- <b>search anything on google</b> by start your speech with ``google`` word. For example : google what is python 

- <b>Can Type</b> : just speak ``Jarvis type`` and wait for assistant to responde, so u can tell what to type

- <b>Ai integration</b> ask any question it will reply with ai
<br>
<br>

<i>NOTE:</i> before give any command to assistant speak ``jarvis`` to wake up the assistant
and then within 5 sec start give the command else after 5 sec u have to again wake up the assistant by saying ``Jarvis``
<br>
<br>




## How To Run Jarvis On Termux or Any Terminal

1. Clone This Repo 
    - ```bash
      git clone https://github.com/nullShubham/jarvis
      ```


2. Navigate To Root Dir
    - ```bash
      cd jarvis
      ```


3. now get your api key from <a href="https://aistudio.google.com/app/apikey">here</a>

4. Create .env File
    - ```bash
      touch .env
      ```

5. open this .env file in the text editor and add 
    - ```
      Key="Your Api Key Goes Here"
      ```
      Example:
    - ```
      Key="AIzaSyDbWG2sxCLYevsr1sZ_O"
      ```

6. Install Requirements
    - ```
      pip install -r requirements.txt
      ```

7. Run The Ai Assistant
    - ```
      python main.py
      ```

8. Now speak ``jarvis`` to start the assistant and everytime before give any command u should speak ``Jarvis``