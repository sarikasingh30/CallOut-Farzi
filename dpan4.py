import json
import random
import string
from datetime import datetime

cities_data = [
    ["New Delhi", 28.6139, 77.2090],
    ["Mumbai", 19.0760, 72.8777],
    ["Bangalore", 12.9716, 77.5946],
    ["Chennai", 13.0827, 80.2707],
    ["Kolkata", 22.5726, 88.3639],
    ["Hyderabad", 17.3850, 78.4867],
    ["Pune", 18.5204, 73.8567],
    ["Ahmedabad", 23.0225, 72.5714],
    ["Jaipur", 26.9124, 75.7873],
    ["Surat", 21.1702, 72.8311],
    ["Lucknow", 26.8467, 80.9462],
    ["Kanpur", 26.4499, 80.3319],
    ["Nagpur", 21.1458, 79.0882],
    ["Indore", 22.7196, 75.8577],
    ["Thane", 19.2183, 72.9781]
]
keys = [
    "mti",
    "processingCode",
    "transactionAmount",
    "dateTimeTransaction",
    "cardholderBillingConversionRate",
    "stan",
    "timeLocalTransaction",
    "dateLocalTransaction",
    "expiryDate",
    "conversionDate",
    "merchantCategoryCode",
    "posEntryMode",
    "acquiringInstitutionCode",
    "forwardingInstitutionCode",
    "rrn",
    "cardAcceptorTerminalId",
    "cardAcceptorId",
    "cardAcceptorNameLocation",
    "cardBalance",
    # "additionalData48",
    "transactionCurrencyCode",
    "cardholderBillingCurrencyCode",
    "posDataCode",
    "originalDataElement",
    "channel",
    "encryptedPan",
    "network",
    # "dcc",
    "kitNo",
    "factorOfAuthorization",
    "authenticationScore",
    "contactless",
    "international",
    "preValidated",
    "enhancedLimitWhiteListing",
    "transactionOrigin",
    "transactionType",
    "isExternalAuth",
    "encryptedHexCardNo",
    "isTokenized",
    "entityId",
    "moneySendTxn",
    "mcRefundTxn",
    "mpqrtxn",
    "authorisationStatus",
    "latitude&longitude",
]

# Function to generate city latitude and longitude
def generate_random_coordinates():
    # Generate a random index within the range of the cities list
    random_index = random.randint(0, len(cities_data) - 1)
    
    # Select a city and its coordinates using the random index
    selected_city = cities_data[random_index]
    
    # Extract city name, latitude, and longitude
    city_name = selected_city[0]
    latitude = selected_city[1]
    longitude = selected_city[2]
    
    return [latitude, longitude]

# Function to generate random string
def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# Function to generate random datetime string
def generate_datetime():
    year = random.randint(2020, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    dt=datetime(year,month,day,hour,minute)
    epoch_time=dt.timestamp()
    return int(epoch_time)


# Function to generate value based on specific condition for each key
def generate_value_for_key(key):
    
    if key == "mti":
        mti = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        return mti # Example value for Message Type Indicator (MTI)
    elif key == "processingCode":
        processing_code = ''.join([str(random.randint(0, 9)) for _ in range(3)])
        return processing_code  # Example value for Processing Code
    elif key == "transactionAmount" or key == "cardBalance":
        return "{:.2f}".format(
            random.uniform(1, 10000)
        )  # Random transaction amount between 1 and 10000 with 2 decimal places
    elif key == "dateTimeTransaction":
        return generate_datetime()  # Random datetime string
    elif key == "cardholderBillingConversionRate":
        conversion_rate = random.uniform(50, 100)
        return "{:.2f}".format(conversion_rate)   # Example value for Cardholder Billing Conversion Rate
    elif key == "stan":
        return str(
            random.randint(10000, 99999)
        )  # Random STAN (System Trace Audit Number)
    elif key == "timeLocalTransaction":
        return f"{random.randint(0, 23):02d}{random.randint(0, 59):02d}{random.randint(0, 59):02d}"  # Random time for local transaction
    elif (
        key == "dateLocalTransaction" or key == "expiryDate" or key == "conversionDate"
    ):
        return f"{random.randint(1, 31):02d}{random.randint(1, 12):02d}"  # Random date representation
    elif key == "merchantCategoryCode":
        mcc = ''.join([str(random.randint(0, 9)) for _ in range(4)])
        return mcc  # Example value for Merchant Category Code
    elif key == "posEntryMode":
        return random.choice(["POS","ONLINE","MOBILE"])  # Example value for POS Entry Mode
    elif key == "acquiringInstitutionCode":
        institution_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return institution_code  # Example value for Acquiring Institution Code
    elif key == "forwardingInstitutionCode":
        institution_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        return institution_code  # Example value for Forwarding Institution Code
    elif key == "rrn":
        return str(
            random.randint(1000000000, 9999999999)
        )  # Random RRN (Retrieval Reference Number)
    elif key == "cardAcceptorTerminalId":
        return str(
            random.randint(10000000, 99999999)
        )  # Random Card Acceptor Terminal ID
    elif key == "cardAcceptorId":
        return str(random.randint(10000000, 99999999)) + " "  # Random Card Acceptor ID
    elif key == "cardAcceptorNameLocation":
        return random.choice(
            [
                "NETFLIXUS",
                "STARBUCKS123",
                "WALMART SUPERCENTER",
                "AMAZON.COM",
                "BEST BUY STORE #567",
                "MCDONALD'S RESTAURANT",
                "TARGET STORE - DOWNTOWN",
                "UBER TECHNOLOGIES INC.",
                "MARRIOTT HOTEL",
                "APPLE STORE - FIFTH AVENUE",
                "SHELL GAS STATION",
                "ELECTRONIC SHOP KINGDOM",
                "FLIPKART.COM",
            ]
        )  # Example value for Card Acceptor Name/Location
    # elif key == "additionalData48":
    #     return "T"  # Example value for Additional Data
    elif key == "transactionCurrencyCode" or key == "cardholderBillingCurrencyCode":
        return random.choice(
            ["USD","EUR","INR"]
        )  # Example value for Currency Code
    elif key == "posDataCode":
        characters = string.ascii_letters + string.digits
        # Generate a random code with the specified length
        pos_data_code = ''.join(random.choices(characters, k=12))
        return pos_data_code  # Example value for POS Data Code
    elif key == "originalDataElement":
        characters = string.ascii_letters + string.digits
        # Generate a random code with the specified length
        original_data_element = ''.join(random.choices(characters, k=16))
        return original_data_element  # Example value for Original Data Element
    elif key == "channel" or key == "transactionOrigin" or key == "transactionType":
        return random.choice(
            ["WEB","MOBILEAPP","ATM"]
        )  # Example value for Channel, Transaction Origin, Transaction Type
    elif key == "encryptedPan":
        return "ZHZ7O0katTAXk23kTwkob9v9UhmAuEMYvYG9b8gR26i"
    elif key == "network":
        return random.choice(["MASTER", "VISA","AMEX"])  # Example value for Network
    elif (
        # key == "dcc"
         key == "contactless"
        or key == "preValidated"
        or key == "enhancedLimitWhiteListing"
        or key == "moneySendTxn"
        or key == "mcRefundTxn"
        or key == "mpqrtxn"
        or key == "isExternalAuth"
        or key == "isTokenized"
        or key == "authorisationStatus" or key == "international"
    ):
        return random.choice(["True", "False"])  # Random boolean value
    elif key == "encryptedHexCardNo":
        return generate_random_string(64)  # Random Encrypted Hex Card Number
    elif key == "entityId":
        return generate_random_string(10)  # Random Entity ID
    elif key == "latitude&longitude":
        arr=generate_random_coordinates()
        return arr
          # Example value for Latitude
    # elif key == "longitude":
        # return "77.216721"  # Example value for Longitude
    else:
        return generate_random_string(10)  # Default random value


# Generate dataset with predefined keys and values based on conditions
dataset = []
for _ in range(10):
    entry = {}
    for key in keys:

        value = generate_value_for_key(key)
        entry[key] = value
    dataset.append(entry)
print(len(dataset))
# Save JSON data to a file
with open("dpan4.json", "w") as json_file:
    json.dump(dataset, json_file, indent=4)

print("Dataset created successfully.")
