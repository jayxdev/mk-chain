import random
from collections import defaultdict

class MarkovChainTextGenerator:
    def __init__(self):
        self.chain = defaultdict(dict)
    
    def train(self, text, n=1):
        """Train the Markov chain on the given text with a context size of `n` words."""
        words = text.split()
        for i in range(len(words) - n):
            # Create the state as a tuple of the current n words
            state = tuple(words[i:i+n])
            next_word = words[i+n]
            # Update the chain with the next word
            if next_word in self.chain[state]:
                self.chain[state][next_word] += 1
            else:
                self.chain[state][next_word] = 1
    
    def generate(self, length=50, seed=None):
        """Generate text of the specified length."""
        if seed:
            random.seed(seed)
        
        # Start with a random state
        current_state = random.choice(list(self.chain.keys()))
        generated_words = list(current_state)
        
        for _ in range(length - len(current_state)):
            current_state = tuple(generated_words[-len(current_state):])
            next_word = self._choose_next_word(current_state)
            if next_word:
                generated_words.append(next_word)
            else:
                break
        
        return ' '.join(generated_words)
    
    def _choose_next_word(self, state):
        """Choose the next word based on the probabilities in the chain."""
        if state in self.chain:
            next_words = self.chain[state]
            total = sum(next_words.values())
            rand_val = random.randint(1, total)
            cumulative = 0
            for word, count in next_words.items():
                cumulative += count
                if rand_val <= cumulative:
                    return word
        return None

# Example usage
if __name__ == "__main__":
    text = """The sun rose over the misty mountains, casting a golden glow across the valley. Birds chirped their morning songs as a gentle breeze rustled through the trees. In the nearby village, people began to stir, preparing for another day of work and play. Children laughed as they ran to school, their backpacks bouncing with each step. Farmers tended to their crops, while shopkeepers opened their doors to welcome customers. The smell of fresh bread wafted from the bakery, enticing passersby. As the day progressed, the bustling town came alive with activity, a testament to the vibrant community that called this place home."""

    generator = MarkovChainTextGenerator()
    generator.train(text, n=2)

    generated_text = generator.generate(length=20)
    print("Generated Text:", generated_text)