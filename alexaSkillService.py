from multiprocessing import Process, Pipe

def sendSensorData(childConnection, sensorDataTuple):
    childConnection.send(sensorDataTuple)
    childConnection.close()


