import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CSV_PATH = "all_floorplans_cupy_raw.csv"


def load_results(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    return df


def analyze_results(df):
    avg_mean_temp = df["mean_temp"].mean()
    avg_std_temp = df["std_temp"].mean()
    n_above_50 = (df["pct_above_18"] >= 50).sum()
    n_below_50 = (df["pct_below_15"] >= 50).sum()

    print(f"Number of buildings: {len(df)}")
    print(f"Average mean temperature: {avg_mean_temp}")
    print(f"Average temperature standard deviation: {avg_std_temp}")
    print(f"Buildings with at least 50% area above 18C: {n_above_50}")
    print(f"Buildings with at least 50% area below 15C: {n_below_50}")


def plot_histograms(df):
    plt.figure()
    plt.hist(df["mean_temp"], bins=30)
    plt.xlabel("Mean temperature")
    plt.ylabel("Number of buildings")
    plt.title("Distribution of mean temperatures")
    plt.tight_layout()
    plt.savefig("mean_temperature_histogram.png", dpi=200)

    plt.figure()
    plt.hist(df["std_temp"], bins=30)
    plt.xlabel("Temperature standard deviation")
    plt.ylabel("Number of buildings")
    plt.title("Distribution of temperature standard deviations")
    plt.tight_layout()
    plt.savefig("std_temperature_histogram.png", dpi=200)


def main():
    df = load_results(CSV_PATH)
    analyze_results(df)
    plot_histograms(df)




if __name__ == "__main__":
    main()