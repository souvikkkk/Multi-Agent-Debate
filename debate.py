from typing import TypedDict, Literal, List

class DebateState(TypedDict):
    topic: str
    current_round: int
    current_agent: Literal["Scientist", "Philosopher"]
    memory: str
    transcript: List[str]
    past_arguments: List[str]

def user_input_node():
    topic = input("Enter topic for debate: ")
    state: DebateState = {
        "topic": topic,
        "current_round": 1,
        "current_agent": "Scientist",
        "memory": "",
        "transcript": [],
        "past_arguments": []
    }
    return state

def agent_node(state: DebateState):
    agent = state["current_agent"]
    round_num = state["current_round"]
    argument = f"This is a sample argument by {agent} in round {round_num}."
    print(f"[Round {round_num}] {agent}: {argument}")
    with open("debate.log", "a") as f:
        f.write(f"[Round {round_num}] {agent}: {argument}\n")
    state["transcript"].append(argument)
    state["past_arguments"].append(argument)
    return state

def memory_node(state: DebateState):
    state["memory"] += state["transcript"][-1] + " "
    return state

def judge_node(state: DebateState):
    print("[Judge] Reviewing debate...")
    summary = " ".join(state["transcript"])
    winner = "Scientist"
    print("[Judge] Summary:", summary)
    print("[Judge] Winner:", winner)
    with open("debate.log", "a") as f:
        f.write("[Judge] Summary: " + summary + "\n")
        f.write("[Judge] Winner: " + winner + "\n")

def main():
    state = user_input_node()

    while state["current_round"] <= 8:
        agent_node(state)
        memory_node(state)
        # Switch agent
        if state["current_agent"] == "Scientist":
            state["current_agent"] = "Philosopher"
        else:
            state["current_agent"] = "Scientist"
        # Increment round
        state["current_round"] += 1

    judge_node(state)

if __name__ == "__main__":
    main()
