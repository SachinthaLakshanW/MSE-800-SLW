import numpy as np

def main():
    # Rainfall data for the week
    rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

    # Convert list to NumPy array
    rain = np.array(rainfall)
    print("Rainfall data:", rain)

    # Total rainfall
    total = np.sum(rain)
    print(f"Total rainfall this week: {total:.2f} mm")

    # Average rainfall
    avg = np.mean(rain)
    print(f"Average rainfall: {avg:.2f} mm")

    # Count of days with no rain
    no_rain = np.sum(rain == 0)
    print(f"Days with no rain: {no_rain}")

    # Days where rainfall was more than 5 mm
    Rain_above_5 = np.where(rain > 5)[0]
    print("Days with more than 5mm of rain:", Rain_above_5)

    # 75th percentile and values above it
    Percentage_75 = np.percentile(rain, 75)
    above_Percentage_75 = rain[rain > Percentage_75]
    print(f"75th percentile: {Percentage_75:.2f} mm")
    print("Rainfall values above 75th percentile:", above_Percentage_75)

if __name__ == "__main__":
    main()