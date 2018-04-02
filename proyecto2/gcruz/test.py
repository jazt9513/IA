import spam_detector

sp=spam_detector.SpamDetector()

d=sp.train_model()

print(d['costs'])
print(d['Y_prediction_test'])
print(d['Y_prediction_train'])
print(d['w'])
print(d['b'])
print(d['learning_rate'])
print(d['num_iterations'])
