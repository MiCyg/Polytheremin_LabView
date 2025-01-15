import numpy as np
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe import solutions



def draw_landmarks_on_image(rgb_image, detection_result):
	hand_landmarks_list = detection_result.hand_landmarks
	annotated_image = np.copy(rgb_image)

	# Loop through the detected hands to visualize.
	for idx, hand_landmarks in enumerate(hand_landmarks_list):
		hand_landmarks = hand_landmarks_list[idx]

		# Draw the hand landmarks.
		hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
		hand_landmarks_proto.landmark.extend([
			landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
		])
		solutions.drawing_utils.draw_landmarks(
			annotated_image,
			hand_landmarks_proto,
			solutions.hands.HAND_CONNECTIONS,
			solutions.drawing_styles.get_default_hand_landmarks_style(),
			solutions.drawing_styles.get_default_hand_connections_style(),
		)

	return annotated_image


def image_32_to_rgb(image32):
	return np.stack([(image32>>16).astype(np.uint8), (image32>>8).astype(np.uint8), (image32>>0).astype(np.uint8)], axis=-1)


def image_rgb_to_32(image):
	image = np.array(image)
	image = image.astype(np.uint32)
	image32 = (image[:, :, 0] << 16) | (image[:, :, 1] << 8) | (image[:, :, 2]<<0)
	return image32

def prepare_for_lv(detection_result):
	out = []
	if detection_result.hand_landmarks!=[]:
		for d_res in detection_result.hand_landmarks[0]:
			out.append([d_res.x, d_res.y, d_res.z])
		out = np.array(out)
		return out




def configure(model_path):
	# MODEL_FILENAME = 'python/hand_landmarker.task'

	global options
	base_options = mp.tasks.BaseOptions(model_asset_path=model_path)
	options = mp.tasks.vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)


def hd_open():
	global detector
	detector = mp.tasks.vision.HandLandmarker.create_from_options(options)

def hd_processing(image32):
	if not image32:
		return np.zeros((21,3)).astype(np.uint32)

	image32 = np.array(image32)
	image = image_32_to_rgb(image32)
	
	mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(image))

	detection_result = detector.detect(mp_image)

	res = prepare_for_lv(detection_result)

	if res is None:
		return np.zeros((21,3)).astype(np.uint32)

	res[:,0] = res[:,0] * image.shape[1]
	res[:,1] = res[:,1] * image.shape[0]
 
	res = res.astype(np.uint32)
 
	return res



def hd_processing_vision(image32):
	image = image_32_to_rgb(np.array(image32))
	
	mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
	

	detection_result = detector.detect(mp_image)
	annotated_image = draw_landmarks_on_image(mp_image.numpy_view()[:,:,:3], detection_result)

	return image_rgb_to_32(annotated_image)

def hd_close():
	detector.close()
	

if __name__=="__main__":
	print("START")
	configure("hand_landmarker.task")
	print("OPEN")
	hd_open()

	test_image = np.zeros((4,8)).astype(np.uint32)
	test_image[:1,:2] = 0xffffffff
	res = image_32_to_rgb(test_image)
	res2 = image_rgb_to_32(res)
 
 
	print("print some values")
	print(test_image)
	print(res)
	print(res2)
	
	print("Processing")
	hd_processing(list(test_image))

	print("Close")
	hd_close()
	print("Yay, functions are working!")