import time

def typing_speed_test():
    passage = "The quick brown fox jumps over the lazy dog"
    print("Type the following passage:")
    print(passage)
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    
    user_input = input("Start typing: ")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    words = passage.split()
    correct_words = user_input.split()
    
    # Calculate the number of correct words typed
    correct_count = sum(1 for a, b in zip(words, correct_words) if a == b)
    
    # Calculate words per minute (WPM)
    wpm = (correct_count / elapsed_time) * 60
    
    print(f"You typed {correct_count} out of {len(words)} words correctly.")
    print(f"Your typing speed is {wpm:.2f} words per minute.")

if __name__ == "__main__":
    typing_speed_test()
    