import time
import random


def generate_ai_response(question):
    """
    Simulates a human-like AI response.
    Replace this function with real GenAI API if needed.
    """

    possible_responses = [
        "I'm doing fine, what about you?",
        "Yeah, I guess so.",
        "idk honestly",
        "Not really sure about that.",
        "That's interesting.",
        "I am good.",
        "Pretty normal day.",
        "I don't care much about it."
    ]

    
    delay = random.uniform(2, 5)
    time.sleep(delay)

    response = random.choice(possible_responses)

    
    if random.random() < 0.3:
        response = response.replace("I'm", "Im")

    return response



def get_human_response():
    return input("Respondent A (Human), type your response: ")



def turing_test():
    print("===================================")
    print("        TURING TEST SYSTEM         ")
    print("===================================\n")

    print("You are the JUDGE.")
    print("You will ask questions to Respondent A and Respondent B.")
    print("One is human, one is machine.\n")

    history_A = []
    history_B = []

    rounds = 3

    for i in range(rounds):
        print(f"\n----- Round {i+1} -----")
        question = input("Judge asks: ")

        
        print("\nRespondent A is typing...")
        response_A = get_human_response()
        history_A.append(response_A)

        
        print("\nRespondent B is typing...")
        response_B = generate_ai_response(question)
        print("Respondent B:", response_B)
        history_B.append(response_B)

    
    print("\n===================================")
    print("        CONVERSATION HISTORY       ")
    print("===================================")

    for i in range(rounds):
        print(f"\nRound {i+1}")
        print("A:", history_A[i])
        print("B:", history_B[i])

   
    print("\nWho is the Human?")
    decision = input("Type A or B: ")

    if decision.upper() == "A":
        print("\nCorrect. Respondent A was the Human.")
    else:
        print("\nIncorrect. Respondent A was the Human.")

    print("\nTest Completed.")


if __name__ == "__main__":
    turing_test()
