

## AI Centre

Researchers with affiliation to the [Pioneer Centre for AI](https://www.aicentre.dk/), can request access to special servers owned by this research group. Three different compute nodes of two types, are owned by this research group:

The nodes `i256-a40-01` and `i256-a40-02` are part of the `aicentre` partition. To launch jobs on these nodes specify:
```
srun --partition=aicentre --account=aicentre hostname
```

The node `nv-ai-04` is part of the `aicentre-a100` partition. To launch jobs on these nodes specify:
```
srun --partition=aicentre-a100 --account=aicentre-a100 hostname
```
