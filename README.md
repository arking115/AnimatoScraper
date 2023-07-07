# Usage

This scraper is designed for the upcoming mvp Animato which feature innovative ai solutions with specific and interactive scientific animations.

It's purpose is to collect and structure web data for this specific niche.

# Set up
- Create a virtual enviroment
```
python3 -m venv myenv
```
- Activate the vritual enviroment:
  - Windows:
    ```
    myenv\Scripts\activate
    ```
  - Unix/Linux:
    ```
    source myenv/bin/activate
    ```
- Install the dependencies:
  ```
  pip3 install -r requirements.txt
  ```
# Start Scraping
  - For the xlsx creation run:
    ```
    python3 scraper.py
    ```
  - For the graph visuals run:
    ```
    python3 generate_graph.py
    ```
# Mentions
This scraper should work of any kind of youtube view's scraping, all the channels which this program collects data from are located in videolinks.py, feel free to modify it based on what channels you want to scrape. Have fun!
