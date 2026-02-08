import grpc
from concurrent import futures
import time

# Импортируем сгенерированные файлы
import course_service_pb2
import course_service_pb2_grpc

class CourseService(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        # Обработчик метода GetCourse
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Сервер запущен на порту 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()