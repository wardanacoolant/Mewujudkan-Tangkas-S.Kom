danceability = []
energy = []
loudness = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
duration_ms = []

with open('Data Fix.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",", quotechar=",", quoting=csv.QUOTE_MINIMAL)
    print(csv_reader)
    for i,row in enumerate(csv_reader):
        if(i>0):
            # print(float(row[6]))
            danceability.append(float(row[3]))
            danceability.append(float(row[4]))
    
    

# Ne Normalisasi Manual
def normalize_list(list_normal):
    max_value = max(list_normal)
    min_value = min(list_normal)
    for i in range(len(list_normal)):
        list_normal[i] = (list_normal[i] - min_value) / (max_value - min_value)
    return list_normal

# Library
def normalize_list_numpy(list_numpy):
    normalized_list = minmax_scale(list_numpy)
    return normalized_list

# Fitur danceability
danceability_array = danceability
danceability_array_numpy = np.array(danceability_array)
print(normalize_list(danceability_array))
print(normalize_list_numpy(danceability_array_numpy))

# Fitur energy
energy_array = danceability
energy_array_numpy = np.array(energy_array)
print(normalize_list(energy_array))
print(normalize_list_numpy(energy_array_numpy))

# Fitur loudness
loudness_array = danceability
loudness_array_numpy = np.array(loudness_array)
print(normalize_list(loudness_array))
print(normalize_list_numpy(loudness_array_numpy))

# Fitur speechiness
speechiness_array = danceability
speechiness_array_numpy = np.array(speechiness_array)
print(normalize_list(speechiness_array))
print(normalize_list_numpy(speechiness_array_numpy))

# Fitur acousticness
acousticness_array = danceability
acousticness_array_numpy = np.array(acousticness_array)
print(normalize_list(acousticness_array))
print(normalize_list_numpy(acousticness_array_numpy))

# Fitur instrumentalness
instrumentalness_array = danceability
instrumentalness_array_numpy = np.array(instrumentalness_array)
print(normalize_list(instrumentalness_array))
print(normalize_list_numpy(instrumentalness_array_numpy))

# Fitur liveness
liveness_array = danceability
liveness_array_numpy = np.array(liveness_array)
print(normalize_list(liveness_array))
print(normalize_list_numpy(liveness_array_numpy))

# Fitur valence
valence_array = danceability
valence_array_numpy = np.array(valence_array)
print(normalize_list(valence_array))
print(normalize_list_numpy(valence_array_numpy))

# Fitur tempo
tempo_array = danceability
tempo_array_numpy = np.array(tempo_array)
print(normalize_list(tempo_array))
print(normalize_list_numpy(tempo_array_numpy))

# Fitur duration_ms
duration_ms_array = danceability
duration_ms_array_numpy = np.array(duration_ms_array)
print(normalize_list(duration_ms_array))
print(normalize_list_numpy(duration_ms_array_numpy))


with open('data baru.csv', 'w') as csv_file:
    csv_wrtiter = csv.writer(new_file, delimiter='\t')