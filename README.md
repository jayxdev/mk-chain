# mk-chain

mk-chain is a Python-based Markov Chain Text Generator that creates new text based on input training data.

## Features

- Generates text using Markov Chain principles
- Customizable context size (n-gram)
- Adjustable output length
- Option to set a random seed for reproducible results

## Installation

Clone the repository:
```git clone https://github.com/yourusername/mk-chain.git cd mk-chain

```
No additional dependencies are required as the project uses only Python standard libraries.

## Usage

### Basic Usage

```python
from main import MarkovChainTextGenerator

# Create an instance of the generator
generator = MarkovChainTextGenerator()

# Train the generator with your text
text = "Your training text goes here..."
generator.train(text, n=2)

# Generate new text
generated_text = generator.generate(length=50)
print(generated_text)```

Advanced Usage
You can customize the following parameters:

`n` in the `train()` method: Sets the context size (n-gram) for the Markov Chain
`length` in the `generate()` method: Determines the number of words in the output
`seed` in the `generate()` method: Sets a random seed for reproducible results
Example:

```generator.train(text, n=3)  # Use trigrams for context
generated_text = generator.generate(length=100, seed=42)```

## How It Works
The `train()` method processes the input text and builds a Markov Chain model.
The `generate()` method uses the trained model to produce new text.
The generator starts with a random state and selects subsequent words based on the probabilities in the chain.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is open source and available under the MIT License.

