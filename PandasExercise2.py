# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:34:00 2022

@author: mcurral
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

#%matplotlib inline

conn = sqlite3.connect('sakila.db')


df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])

df.head()

df['film_rental_duration'].mean()

df['film_rental_duration'].value_counts().plot(kind='bar', figsize=(14,6))

df['film_rental_duration'].value_counts() # probably number of rental during in days!

pd.set_option('display.max_columns', None)

#df['film_rental_duration'].plot(kind='box', vert=False, figsize=(14,6))
df['film_replacement_cost'].plot(kind='box', vert=False, figsize=(14,6))
df['film_replacement_cost'].value_counts().plot(kind='bar', figsize=(14,6))

# lol... antes tinha:  rental_rate(),  e a juntar à festa..:  .value_counts()  ---- LOL
ax = df['film_replacement_cost'].plot(kind = 'density', figsize = (15,8)) 
# df.columns
#df['film_rental_rate'].value_counts()
ax.axvline(df['film_replacement_cost'].mean(), color='red')
ax.axvline(df['film_replacement_cost'].median(), color='green')
ax.axvline(df['film_replacement_cost'].mode().values[0], color='black') # podem haver mais que um moda

df['film_rating'].value_counts() #df.columns
df['film_rating'].value_counts().plot(kind='bar', figsize=(12,6))




df[['film_rating', 'film_replacement_cost']].boxplot(by='film_rating')#, figsize=(14,6)) # com o by passa de um para vários... é parecido com o value_counts()
df[['film_rating', 'film_replacement_cost']].boxplot(by='film_rating', figsize=(14,6))


df['rental_days2'] = df['return_date'] - df['rental_date']
#type(df['rental_days']) # surte mais efeitos: df.rental_days ou df['rental_days']

df['rental_days'] = df[['rental_date', 'return_date']].apply(lambda x: (x[1] - x[0]).days,axis=1)

df['rental_days'].mean()

ax = df['rental_days'].plot(kind='kde', figsize = (14,6))
ax.axvline(df['rental_days'].mean(), color = 'brown')
ax.axvline(df['rental_days'].median(), color = 'yellow')
ax.axvline(df['rental_days'].mode().values[0], color = 'grey')

df['film_daily_rental_rate'] = df[['film_rental_rate', 'film_rental_duration']].apply(lambda x: (x[0] / x[1]), axis=1)

df['film_daily_rental_rate2'] = df['film_rental_rate'] / df['film_rental_duration']

df['film_daily_rental_rate2'].head()