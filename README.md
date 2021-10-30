# 4IZ460
Datamining Spotify datasetu pro předmět 4IZ460.

## Analytické otázky
1.	Mají taneční skladby výrazně větší hitový potenciál? Mění se tento potenciál v závislosti na dekádě?
2.	Jaké faktory nejvíce korelují s faktem, že se skladba stala hitem?
3.	Existuje vazba valence (pozitivity/negativity) na období, která se vyznačují negativními událostmi (např. 2008, 2001)?
4.	Existuje konkrétní tónina/skupina tónin, která výrazně převažuje mezi hity?
5.	Jak moc ovlivňuje instrumentálnost, přítomnost mluveného slova a způsob nahrávání skladeb jejich výslednou popularitu?
6.	Jaké faktory určují, zda autor dosáhl vysokého počtu hitů za svou kariéru?

## Struktura repozitáře
Ve složce data se nachází dataset z [Kaggle](https://www.kaggle.com/theoverman/the-spotify-hit-predictor-dataset). Ve složce examples jsou skripty pro základní spuštění clevermineru.

## Spouštění

pip install spotipy
pip install cleverminer==0.082
pip install spotipy
pip install pprint
```

## Odkazy
Spotify API - https://developer.spotify.com/dashboard/

## Základní přehled o datasetu

### Deskriptivní statistiky

```csv
Unnamed: 0  danceability        energy           key      loudness          mode   speechiness  acousticness  instrumentalness      liveness       valence         tempo   duration_ms  time_signature    chorus_hit      sections           hit           era
count  41106.000000  41106.000000  41106.000000  41106.000000  41106.000000  41106.000000  41106.000000  41106.000000      41106.000000  41106.000000  41106.000000  41106.000000  4.110600e+04    41106.000000  41106.000000  41106.000000  41106.000000  41106.000000
mean   20552.500000      0.539695      0.579545      5.213594    -10.221525      0.693354      0.072960      0.364197          0.154416      0.201535      0.542440    119.338249  2.348776e+05        3.893689     40.106041     10.475673      0.500000     52.925607
std    11866.424419      0.177821      0.252628      3.534977      5.311626      0.461107      0.086112      0.338913          0.303530      0.172959      0.267329     29.098845  1.189674e+05        0.423073     19.005515      4.871850      0.500006     32.562672
min        0.000000      0.000000      0.000251      0.000000    -49.253000      0.000000      0.000000      0.000000          0.000000      0.013000      0.000000      0.000000  1.516800e+04        0.000000      0.000000      0.000000      0.000000      0.000000
25%    10276.250000      0.420000      0.396000      2.000000    -12.816000      0.000000      0.033700      0.039400          0.000000      0.094000      0.330000     97.397000  1.729278e+05        4.000000     27.599793      8.000000      0.000000     10.000000
50%    20552.500000      0.552000      0.601000      5.000000     -9.257000      1.000000      0.043400      0.258000          0.000120      0.132000      0.558000    117.565000  2.179070e+05        4.000000     35.850795     10.000000      0.500000     60.000000
75%    30828.750000      0.669000      0.787000      8.000000     -6.374250      1.000000      0.069800      0.676000          0.061250      0.261000      0.768000    136.494000  2.667730e+05        4.000000     47.625615     12.000000      1.000000     80.000000
max    41105.000000      0.988000      1.000000     11.000000      3.744000      1.000000      0.960000      0.996000          1.000000      0.999000      0.996000    241.423000  4.170227e+06        5.000000    433.182000    169.000000      1.000000     90.000000
```