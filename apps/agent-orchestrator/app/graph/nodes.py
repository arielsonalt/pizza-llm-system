async def classify(state: dict):
    state["intent"] = "question"
    return state

async def answer(state: dict):
    return {
        "response": "This is a placeholder pizza assistant response."
    }
