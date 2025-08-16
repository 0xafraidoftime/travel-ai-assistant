# Conversational AI Travel Assistant

A comprehensive travel assistant chatbot built with Python that combines natural language understanding, database integration, API handling, and personalized recommendations to provide seamless travel booking and support services.

## Project Files

- **`CAI.ipynb`**: Original Jupyter notebook with complete implementation and examples
- **`cai.py`**: Standalone Python script extracted from the notebook
- **`create_database.py`**: Database setup script with sample data
- **`requirements.txt`**: All required Python packages
- **`travel_info.db`**: SQLite database (auto-generated)

## Features

### Natural Language Understanding (NLU)
- **Entity Recognition**: Automatically extracts dates, locations, and other relevant entities from user input
- **Intent Detection**: Rule-based system to classify user intents (flight booking, hotel inquiries, general questions)
- **Powered by spaCy**: Uses the `en_core_web_sm` model for robust text processing

### Conversational AI
- **BlenderBot Integration**: Utilizes Facebook's BlenderBot-400M-distill model for natural conversations
- **Context-Aware Responses**: Generates relevant responses based on travel-related queries
- **Hugging Face Transformers**: Leverages state-of-the-art transformer models

### Database Management
- **SQLite Integration**: Local database for storing flight schedules and booking information
- **Flight Data Storage**: Manages flight numbers, destinations, dates, and times
- **Query Functionality**: Efficient retrieval of flight information based on user criteria

### API Integration
- **Amadeus Travel API**: Real-world flight search and booking capabilities
- **OAuth2 Authentication**: Secure API access with proper token management
- **Flight Search**: Search for flights between origin and destination with specific dates

### Personalized Recommendations
- **Preference-Based Suggestions**: Recommends destinations based on user preferences
- **Category Matching**: Handles different travel types (beach, adventure, cultural)
- **Customizable Logic**: Easy to extend with additional recommendation algorithms

### Booking Management
- **Flight Booking**: Complete booking workflow with user details
- **Cancellation Support**: Handle booking cancellations with confirmation
- **User Data Management**: Store and manage customer information

### Real-Time Updates & Support
- **Flight Status Updates**: Real-time flight delay and status information
- **Customer Support**: FAQ-based support system for common queries
- **Automated Responses**: Instant answers to frequently asked questions

## Getting Started

### Option 1: Jupyter Notebook (Recommended for Development)
1. Open `CAI.ipynb` in Jupyter Notebook or Google Colab
2. Run cells sequentially to install dependencies and execute code
3. The notebook includes detailed explanations and examples for each task

### Option 2: Python Script
1. Follow the Quick Setup instructions below
2. Run `python cai.py` to execute the complete application

### Option 3: Google Colab
1. Upload `CAI.ipynb` to Google Colab
2. All dependencies can be installed directly in the notebook
3. Perfect for experimentation and testing

## Installation

### Prerequisites
- Python 3.7+ (for script execution)
- Jupyter Notebook or Google Colab (for notebook usage)
- pip package manager

### Quick Setup
```bash
# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Create and populate database
python create_database.py

# Run the application
python cai.py
```

### Manual Package Installation
```bash
pip install spacy transformers datasets requests
python -m spacy download en_core_web_sm
```

### API Setup
1. **Amadeus API Credentials**:
   - Sign up at [Amadeus Developer Portal](https://developers.amadeus.com/)
   - Replace `API_KEY` and `API_SECRET` in the code with your credentials
   - Use test environment initially: `https://test.api.amadeus.com`

## Usage

### Basic NLU Processing
```python
user_input = "I want to book a flight to New York on September 21"
intent = process_input(user_input)
print(f"Detected Intent: {intent}")
```

### Chatbot Conversation
```python
user_input = "I'm looking for a flight to Paris next week"
response = chatbot_response(user_input)
print(f"Chatbot: {response}")
```

### Flight Search
```python
# Query local database
query_flight('New York', '2024-09-21')

# Search via API (requires valid credentials)
flight_offers = get_flight_offers_mock("LAX", "JFK", "2024-10-15")
```

### Booking Management
```python
user_details = {'name': 'John Doe', 'email': 'john@example.com'}
booking_result = book_flight('AA123', user_details)
cancellation_result = cancel_booking('ABC123')
```

### Travel Recommendations
```python
user_preferences = ['beach', 'luxury']
recommendation = recommend_destination(user_preferences)
print(recommendation)
```

## Project Structure

```
travel-ai-assistant/
├── CAI.ipynb             # Jupyter notebook (original development)
├── cai.py                # Main Python application file
├── create_database.py    # Database setup and population script
├── travel_info.db        # SQLite database (created by setup script)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Development Workflow

### For Jupyter Notebook Development
1. Open `CAI.ipynb` in your preferred environment
2. Each task is organized in separate cells with explanations
3. Modify and experiment with individual components
4. Use the notebook for prototyping and testing

### For Production Deployment
1. Use `cai.py` as the main application script
2. Run `create_database.py` first to set up data
3. Configure API credentials in environment variables
4. Deploy as a standalone Python application

### File Relationships
- `CAI.ipynb` → Original development notebook
- `cai.py` → Extracted production-ready script  
- `create_database.py` → Database initialization
- `requirements.txt` → Dependency management

### 1. Natural Language Processing
- **spaCy NLP Pipeline**: Entity recognition and text processing
- **Intent Classification**: Rule-based intent detection system
- **Entity Extraction**: Automatic extraction of travel-related entities

### 2. Conversational Interface
- **BlenderBot Model**: Pre-trained conversational AI model
- **Response Generation**: Context-aware response generation
- **Pipeline Integration**: Streamlined text generation workflow

### 3. Data Management
- **SQLite Database**: Lightweight, file-based database
- **Flight Records**: Structured storage of flight information
- **Query Interface**: SQL-based data retrieval

### 4. External APIs
- **Amadeus Integration**: Professional travel API access
- **Authentication Flow**: OAuth2 token management
- **Error Handling**: Robust API error management

### 5. Business Logic
- **Recommendation Engine**: Preference-based destination suggestions
- **Booking Workflow**: Complete booking and cancellation process
- **Support System**: Automated customer support responses

## Core Components

### Environment Variables
```bash
export AMADEUS_API_KEY="your_api_key_here"
export AMADEUS_API_SECRET="your_api_secret_here"
```

### Database Setup
The project includes a comprehensive database setup script:

```bash
python create_database.py
```

This creates `travel_info.db` with three tables:
- **flights**: Flight schedules, prices, and availability
- **bookings**: Customer booking records
- **users**: User profiles and preferences

The script populates the database with realistic sample data including:
- 10 sample flights across major routes
- 5 example bookings with different statuses
- 5 user profiles with various travel preferences

## Configuration

### Amadeus API
- **Authentication**: `POST /v1/security/oauth2/token`
- **Flight Search**: `GET /v2/shopping/flight-offers`

## API Endpoints Used

### Adding New Intents
```python
def detect_intent(user_input):
    if "book a flight" in user_input.lower():
        return "Booking Flight"
    elif "hotel" in user_input.lower():
        return "Hotel Inquiry"
    elif "car rental" in user_input.lower():  # New intent
        return "Car Rental"
    return "General Inquiry"
```

### Custom Recommendation Logic
```python
def advanced_recommend_destination(preferences, budget, season):
    # Implement complex recommendation logic
    pass
```

## Extending the System

## Troubleshooting

### Common Issues
1. **spaCy Model Not Found**: Run `python -m spacy download en_core_web_sm`
2. **API Authentication Errors**: Verify your Amadeus API credentials in the notebook/script
3. **Database Lock**: Ensure proper connection closure after operations
4. **Memory Issues**: Consider using smaller transformer models for limited resources
5. **Jupyter Kernel Issues**: Restart kernel if encountering import errors
6. **Package Conflicts**: Use virtual environment for clean installation

### Notebook-Specific Issues
- **Cell Execution Order**: Run cells in sequential order for proper initialization
- **Colab Environment**: Some packages may need reinstallation in new Colab sessions
- **File Paths**: Ensure database file paths are correct when switching between environments

### Error Handling
The system includes basic error handling for:
- API request failures
- Database connection issues
- Invalid user input
- Missing model files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **spaCy**: For natural language processing capabilities
- **Hugging Face**: For transformer models and tokenizers
- **Amadeus**: For travel API services
- **Facebook AI**: For the BlenderBot conversational model

## Future Enhancements

- [ ] Multi-language support
- [ ] Voice interface integration
- [ ] Machine learning-based intent classification
- [ ] Hotel and car rental booking
- [ ] Payment gateway integration
- [ ] Mobile application development
- [ ] Advanced analytics and reporting
