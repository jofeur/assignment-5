# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils

def main():
    dev_path = "birth_dev.tsv"
    with open(dev_path, encoding="utf-8") as fin:
        n = len(fin.readlines())
    predictions = ["London"] * n
    total, correct = utils.evaluate_places(dev_path, predictions)
    accuracy = (correct / total) * 100.0 if total > 0 else 0.0

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
