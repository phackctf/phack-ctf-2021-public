# Enchaîné
## Challenge

Lors de votre phase de reconnaissance, vous avez trouvé une chaîne de caractères étrange :

`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJQSGFja0NURiIsImlhdCI6MTYxNzM4NjQwMCwiZXhwIjoxNjE4MTY0MDAwLCJhdWQiOiIiLCJzdWIiOiIiLCJmbGFnIjoiNTEzMTU2NGY1NTQ2NjgzNzVhMzM1NTc4NWE2YzM4Nzc1OTU0NGU2NjYxNmE1MjZkNTgzMTU2MzI1NTU2NDU3YTU5NTgzMDNkIn0.XsPHPbpV2oHwi8t1dPXblJ2IokuUNhJywOyqKdFB9cw`

Il vous semble connaître ce format, mais sans certitude.


## Résolution

C'est un token JWT :
`eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJQSGFja0NURiIsImlhdCI6MTYxNzM4NjQwMCwiZXhwIjoxNjE4MTY0MDAwLCJhdWQiOiIiLCJzdWIiOiIiLCJmbGFnIjoiNTEzMTU2NGY1NTQ2NjgzNzVhMzM1NTc4NWE2YzM4Nzc1OTU0NGU2NjYxNmE1MjZkNTgzMTU2MzI1NTU2NDU3YTU5NTgzMDNkIn0.XsPHPbpV2oHwi8t1dPXblJ2IokuUNhJywOyqKdFB9cw`

**From JWT**
```
{
  "iss": "PHackCTF",
  "iat": 1617386400,
  "exp": 1618164000,
  "aud": "",
  "sub": "",
  "flag": "5131564f554668375a3355785a6c387759544e66616a526d583156325556457a5958303d"
}
```

**From Hex**
Q1VOUFh7Z3UxZl8wYTNfajRmX1V2UVEzYX0=

**From base64**
CUNPX{gu1f_0a3_j4f_UvQQ3a}

**From ROT13**
PHACK{th1s_0n3_w4s_HiDD3n}

# Setup

Description.

## Flag
`PHACK{th1s_0n3_w4s_HiDD3n}`