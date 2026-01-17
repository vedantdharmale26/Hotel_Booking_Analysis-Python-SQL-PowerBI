import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/hotel_bookings_sample_550.csv")

df.head()
df.shape
df.info()
df.describe()

df.isnull().sum()
df['is_canceled'] = df['is_canceled'].astype(int)
df['arrival_date_year'] = df['arrival_date_year'].astype(int)

df = df[df['adr'] > 0]
df['total_stay_nights'] = (
    df['stays_in_week_nights'] + df['stays_in_weekend_nights']
)

df['booking_status'] = df['is_canceled'].map({
    0: 'Not Canceled',
    1: 'Canceled'
})

df['is_canceled'].mean() * 100
df.groupby('hotel')['is_canceled'].mean() * 100
df[df['is_canceled']==0].groupby('hotel')['adr'].mean()
df.groupby('arrival_date_month').size()

df['hotel'].value_counts().plot(kind='bar')
plt.title("Bookings by Hotel Type")
plt.show()

df['booking_status'].value_counts().plot(
    kind='pie', autopct='%1.1f%%'
)
plt.show()

df.to_csv("data/cleaned_hotel_bookings.csv", index=False)

