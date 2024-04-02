def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            line = line.replace(',', '.').split()
            attributes = list(map(float, line[:-1]))
            decision_attribute = line[-1]
            data.append([attributes, decision_attribute])
    return data


def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))


def perceptron_train(train_data, learning_rate, class_to_learn):
    weights = [0.1] * len(train_data[0][0])
    bias = 0
    ileprzebiegow = 0
    while True:
        isFalse = 0
        for instance in train_data:
            x, y = instance[0], instance[1]
            predicted = dot_product(weights, x) + bias
            if predicted >= 0:
                predicted = 1
            else:
                predicted = 0

            y = 1 if y == class_to_learn else 0
            if y != predicted: isFalse += 1
            error = y - predicted
            weights = [wi + learning_rate * error * xi for wi, xi in zip(weights, x)]
            bias += learning_rate * error
        ileprzebiegow += 1

        if isFalse == 0:
            break
    print(ileprzebiegow)
    return weights, bias


def perceptron_predict(instance, weights, bias):
    predicted = dot_product(weights, instance) + bias
    if predicted >= 0:
        return 1
    else:
        return 0

def main():
    training_data = read_file("iris_training.txt")
    test_data = read_file("iris_test.txt")

    learning_rate = 0.1
    class_to_learn = "Iris-setosa"
    weights, bias = perceptron_train(training_data, learning_rate, class_to_learn)
    print(weights, bias)

    positive_test = 0
    all_tests = len(test_data)
    for test_instance in test_data:
        expected_value = 1 if test_instance[1] == class_to_learn else 0
        real_value = perceptron_predict(test_instance[0], weights, bias)
        positive_test += (1 if expected_value == real_value else 0)
        print("Expected value:", expected_value, "Predicted value:", real_value)

    print("Number of positive tests =", positive_test, "out of", all_tests)
    print("Test correctness =", round(positive_test / all_tests, 3) * 100, '%')

    while True:
        try:
            attributes_input = input("Enter attributes separated by white space (e.g., 5.1 3.5 1.4 0.2): ").replace(',',
                                                                                                                    '.')

            if len(attributes_input.split()) == 0: raise ValueError
            attributes = list(map(float, attributes_input.split()))
            predicted_label = perceptron_predict(attributes, weights, bias)
            print("Predicted label:", "Iris-setosa" if predicted_label == 1 else "Not Iris-setosa")
            continue_input = input("Do you want to continue (y/n)? ").strip().lower()
            if continue_input != 'y':
                break
        except ValueError:
            print("You typed wrong values")


main()
