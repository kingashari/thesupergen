# The SuperGen: Randomized Bet Number Generator with AI Integration

The SuperGen is a Python-based tool designed to generate randomized betting combinations using web scraping and AI-based predictions. This application scrapes numbers from specific sources and integrates AI data to partially replace numbers in the generated combinations, adding an extra layer of unpredictability. 

## Features
- **Scraping Dead Numbers**: Automatically scrapes "dead numbers" (numbers not to use in the combinations) from a specified URL, helping to avoid unwanted results.
- **AI-Based Number Modification**: Fetches AI-generated numbers from a web source to replace a few digits in the combinations, adding randomness and unpredictability.
- **Flexible Combinations**: Supports generating combinations for 4D, 3D, and 2D bets with customized betting amounts.
- **Randomization**: Each combination is shuffled and randomized, ensuring unique and varied outputs every time.

## How It Works
1. **Scraping Dead Numbers**: The script fetches "dead numbers" from `https://www.belatiaksara4d.com`, avoiding these numbers in the final combinations.
2. **Scraping AI Numbers**: It pulls AI-generated numbers from `https://w33.angkanet.fit/kalender-togel/`, which are partially mixed into the combinations.
3. **Generating Combinations**: Based on user input, the script generates combinations for 4D, 3D, and 2D bets.
4. **AI Integration**: The generated combinations are partially modified by numbers from the AI data to create mixed, unique results.
5. **Output**: The final result displays combinations for 4D, 3D, and 2D bets in the required format.

## Usage
1. **Requirements**: Make sure you have `requests` and `BeautifulSoup4` installed. You can install them using:
   ```bash
   pip install requests beautifulsoup4
   ```
2. **Run the Script**:
   ```bash
   python thesupergen.py
   ```
3. **Input Details**:
   - Enter the number of combinations to generate.
   - Specify betting amounts for 4D, 3D, and 2D.
4. **Output Example**:
   ```
   4D: 2043*2430*4283*4832#1+
   3D: 043*034*283*238#1+
   2D: 43*34*83*38#1
   ```
   This shows the generated numbers with AI-mixed digits for betting.

## Code Overview
- **`scrape_nomer_tidak_keluar`**: Scrapes "dead numbers" to avoid using them in generated combinations.
- **`scrape_data_ai`**: Fetches AI-generated numbers based on the current date.
- **`generate_kombinasi`**: Generates combinations by avoiding dead numbers.
- **`gabung_data_ai`**: Partially replaces digits in combinations with AI data, adding randomness.
- **`main`**: Main function that drives the program, taking user inputs and displaying the results.

## Future Improvements
- Add more customization for AI data integration (e.g., percentage of numbers replaced).
- Enhance error handling for scraping operations.
- Support more betting formats and additional scraping sources.
