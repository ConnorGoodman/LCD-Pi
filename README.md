# README

## Display Message on Raspberry Pi Zero W 2

This Python script is designed to run on a Raspberry Pi Zero W 2 with an attached LCD display. The script fetches a message from an Azure Blob Storage URL and displays it on the LCD screen. The message is split into lines of text, with each line containing a maximum of 16 characters.

### Prerequisites

Before running the script, ensure you have the following:

1. **Raspberry Pi Zero W 2:** This script is specifically designed for the Raspberry Pi Zero W 2. Ensure that your hardware is set up correctly.

2. **LCD Display:** The script uses the `drivers` library for communication with the LCD display. Make sure your LCD display is properly connected to the Raspberry Pi.

3. **Azure Blob Storage Account:** You need an Azure Blob Storage account with a container containing the desired message. Set the URL of the blob storage in the script by setting the `AZURE_BLOB_URL` environment variable.

4. **Python Libraries:** Install the necessary Python libraries using the following command:

   ```bash
   pip install requests python-dotenv
   ```

### Configuration

1. **Environment Variables:**

   Create a `.env` file in the same directory as the script and set the following environment variables:

   ```env
   AZURE_BLOB_URL=<your_blob_url>
   ```

   Replace `<your_blob_url>` with the actual URL of your Azure Blob Storage.

### Running the Script

1. **Make the Script Executable:**

   Ensure the script has execute permissions:

   ```bash
   chmod +x script_name.py
   ```

   Replace `script_name.py` with the actual name of your script.

2. **Run the Script:**

   Execute the script using the following command:

   ```bash
   python main.py
   ```


### Script Behavior

- The script continuously fetches the message from Azure Blob Storage and updates the LCD display every 2 seconds.

- If the message is longer than 16 characters, the script intelligently breaks it into multiple lines to fit the display.

- The script will keep running indefinitely, fetching and displaying messages from the Azure Blob Storage URL.

### Troubleshooting

- If you encounter any issues, check the console output for error messages.

- Ensure that the Raspberry Pi Zero W 2 is connected to the internet.

- Verify the correct setup of the LCD display and its connection to the Raspberry Pi.

- Ensure the Azure Blob Storage URL is correctly set in the `.env` file.

### Notes

- This script is designed for a specific hardware setup (Raspberry Pi Zero W 2 with an LCD display) and Azure Blob Storage usage. Modify it according to your specific requirements.

- Always handle sensitive information, such as Azure Blob Storage access credentials, securely.

Feel free to customize the script as needed for your specific use case.
