# 1337-fish-rng: RNG from Live Fish Movements

## Overview

1337-fish-rng is an innovative project that uses live video streams from the Monterey Bay Aquarium to generate random numbers based on fish movements. This unique approach to randomness leverages the unpredictability of natural processes in a creative and engaging way.

## Concept

Drawing from concepts like atmospheric noise and radioactive decay used in traditional randomness generation, 1337-fish-rng captures the chaotic movement of fish to provide a source of entropy. This method contrasts sharply with algorithmic randomness, offering a fresh perspective on generating truly random numbers.

## History

Historically, the utilization of natural phenomena for generating randomness has seen applications in various scientific and encryption-related fields. The 1337-fish-rng project taps into this rich vein by observing and quantifying the random paths of fish in an aquarium environment.

## Considerations for Production Use

### Security and Reliability

- **Entropy Source**: The randomness quality is contingent upon the continuous and stable observation of fish movements.
- **Manipulation Risks**: Potential predictability and external influence on fish behavior pose risks.

### Performance Concerns

- **Computation Intensity**: Video processing demands significant computational resources, which may affect throughput and latency.
- **Scalability Challenges**: Scaling a video analysis-based service could present unique technical challenges.

### Additional Entropy Sources

Enhancing the randomness involves integrating more entropy sources such as:
- **Environmental Sensors**: Adding data from ambient environment sensors to enrich the entropy pool.
- **Hybrid RNG Systems**: Merging fish-based randomness with other digital noise sources, like hardware random generators, can improve the robustness and security.

## Docker Setup

### Building the Docker Image

From the project's root directory, build the Docker image:
```bash
docker build -t 1337-fish-rng .
```

### Running the Container

To run the Docker container:
```bash
docker run -p 8000:8000 1337-fish-rng
```

This makes the application accessible at `http://localhost:8000`. API documentation is available at `http://localhost:8000/docs`.

## GitHub Repository

The project is maintained on GitHub by `copyleftdev`. Visit [copyleftdev/1337-fish-rng](https://github.com/copyleftdev/1337-fish-rng) for source code, updates, and contribution guidelines.

## Conclusion

1337-fish-rng is a thought-provoking experiment in randomness generation. While it holds potential for educational and experimental applications, further research and development are needed for high-stakes environments such as cryptographic applications.
