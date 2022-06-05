import os
import yaml
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generative Models')
    parser.add_argument('--config', 
                        '-c', 
                        dest='filename', 
                        metavar='FILE', 
                        help='path to config file', 
                        default='configs/vae.yaml')

    args = parser.parse_args()
    with open(args.filename, 'r') as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)