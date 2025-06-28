# Multi-Agent-Debate

## 📌 Project Overview 
Constructing a debate simulation system using LangGraph where two AI agents engage in a
structured argument over a fixed topic. The system should use memory, control over turns,
and a judging node that evaluates the debate logically and declares a winner.

## 🎯 Objectives
Design and implement a LangGraph-based workflow with two alternating agents debating a
fixed topic. The system should preserve and summarize the dialogue history, validate logical
progression, and end with an automated judgment using a dedicated node.

# 📂 Project Structure
Multi Agent Debate/      
├── deabte.py              --> Model loading   
├── debate.log             --> Stores the debate information    
└── README.md              --> Project documentation 

# ⚙️ Setup Instructions   
  ### Create a Python virtual environment  
      - python train_lora.py      
      - debateenv\Scripts\activate

  ###  Install dependencies
      - pip install -r requirements.txt

  ### Set API
      - Go to site https://platform.openai.com/ and create an API.    
      - Load it using the terminal.    
  
  ### Run the model
      - python debate.py   

# 🧪 Sample Interaction
Enter topic for debate: Should AI be regulated like medicine?     
Starting debate between Scientist and Philosopher...     
[Round 1] Scientist: AI must be regulated due to high-risk applications.    
[Round 2] Philosopher: Regulation could stifle philosophical progress and autonomy.    
...    
[Round 8] Philosopher: History shows overregulation often delays societal evolution.    
[Judge] Summary of debate:   
...        
[Judge] Winner: Scientist        
