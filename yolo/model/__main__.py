from ultralytics import YOLO
from pathlib import Path

def main():

    # txts = list(Path("dataset", "labels", "train_white").glob("**/*.txt")) 
    # txts_stems = []
    # for txt in txts:
    #     txts_stems.append(txt.stem)

    # images = list(Path("dataset", "images", "train_white").glob("**/*.png")) 
    # for i, image in enumerate(images):
    #     if image.stem not in txts_stems: print(f"{i:} {image}")
    
    # 277 dataset/images/train_white/lc6986065-1.png
    # 748 dataset/images/train_white/lc6986302-6.png
    # 790 dataset/images/train_white/lc6986302-1.png
    # 3118 dataset/images/train_white/lc6987705-1.png
    # 3175 dataset/images/train_white/lc6986302-4.png
    # 3215 dataset/images/train_white/lc6986302-3.png
    # 3711 dataset/images/train_white/lc6986065-3.png
    # 3974 dataset/images/train_white/lc6986302-2.png
    # 4108 dataset/images/train_white/lc6986302-5.png
    # 4716 dataset/images/train_white/lc6986065-2.png


    # Load a model
    # model = YOLO("yolov8n.yaml")  # build a new model from scratch

    # Use the model
    # path_config = Path("model", "config.yaml")
    # path_config = Path("dataset", "config_staff_augm_all.yaml")
    # path_config = Path("dataset", "config_staff_white.yaml")
    # path_config = Path("dataset", "config_staff_without_back.yaml")
    # path_config = Path("dataset", "config_staff_without_caligraph.yaml")
    # path_config = Path("dataset", "config_staff_without_kanungo.yaml")
    # path_config = Path("dataset", "config_staff_without_seep.yaml")

    # path_config = Path("dataset", "config_staffMeasure_augm_all.yaml")
    # path_config = Path("dataset", "config_staffMeasure_white.yaml")
    # path_config = Path("dataset", "config_staffMeasure_without_back.yaml")
    # path_config = Path("dataset", "config_staffMeasure_without_caligraph.yaml")
    # path_config = Path("dataset", "config_staffMeasure_without_kanungo.yaml")
    # path_config = Path("dataset", "config_staffMeasure_without_seep.yaml")

    # path_config = Path("dataset", "config_noteheads_augm_all.yaml")
    # path_config = Path("dataset", "config_noteheads_2xLargerBBox_augm_all.yaml")
    # path_config = Path("dataset", "config_noteheads_3xLargerBBox_augm_all.yaml")


    # model.train(data=str(path_config), epochs=20, imgsz=640, device=0)  # train the model



    # Eval:

    # model = YOLO("runs/detect/train60/weights/best.pt")   
    # model = YOLO("runs/detect/train52/weights/best.pt")

    # # Staff:
    # model = YOLO("runs/detect/train65/weights/best.pt")     # augm_all
    # model = YOLO("runs/detect/train64/weights/best.pt")     # white
    # model = YOLO("runs/detect/train66/weights/best.pt")     # back
    # model = YOLO("runs/detect/train67/weights/best.pt")     # caligraph
    # model = YOLO("runs/detect/train68/weights/best.pt")     # kanungo
    # model = YOLO("runs/detect/train69/weights/best.pt")     # seep

    # # StaffMeasure:
    # model = YOLO("runs/detect/train70/weights/best.pt")     # augm_all
    # model = YOLO("runs/detect/train71/weights/best.pt")     # white
    # model = YOLO("runs/detect/train71/weights/best.pt")     # back
    # model = YOLO("runs/detect/train72/weights/best.pt")     # caligraph
    # model = YOLO("runs/detect/train73/weights/best.pt")     # kanungo
    model = YOLO("runs/detect/train74/weights/best.pt")     # seep




    # metrics = model.val(data="dataset/config_eval_staff.yaml")   
    metrics = model.val(data="dataset/config_eval_staffMeasure.yaml")

    # metrics = model.val()
    # results = model("dataset/train_augm_all/images/lc4904021-1.jpg")
    results = model([
        "dataset/eval/images/70fac7dd-90e8-4e7b-b12f-0b0c1ccbca00_130_287_1890_2571.jpg",
        "dataset/eval/images/3997e154-a7bc-41d8-9bf2-089c50187b10_131_112_2925_3804.jpg",
        "dataset/eval/images/cc8bc884-ae43-4a26-8914-4f988bec7bb6_63_168_2543_3142.jpg",
        "dataset/eval/images/IMSLP14816-005-004.png",
        "dataset/eval/images/IMSLP85424-009-008.png",
        "dataset/eval/images/IMSLP511349-013-012.png"
    ])

    # print(f"MAP: {metrics.box.map}")  
    # print(results[0].boxes.xywh) #tensor([], size=(0, 4))
    # print(results[0].boxes.cls)

    for i, result in enumerate(results):
        # result.save(filename=f"results/Staff_augm_all/result{i}.jpg")
        # result.save(filename=f"results/Staff_white/result{i}.jpg")
        # result.save(filename=f"results/Staff_back/result{i}.jpg")
        # result.save(filename=f"results/Staff_caligraph/result{i}.jpg")
        # result.save(filename=f"results/Staff_kanungo/result{i}.jpg")
        # result.save(filename=f"results/Staff_seep/result{i}.jpg")

        # result.save(filename=f"results/Measures_augm_all/result{i}.jpg")
        # result.save(filename=f"results/Measures_white/result{i}.jpg")
        # result.save(filename=f"results/Measures_back/rresult{i}.jpg")
        # result.save(filename=f"results/Measures_caligraph/result{i}.jpg")
        # result.save(filename=f"results/Measures_kanungo/result{i}.jpg")
        result.save(filename=f"results/Measures_seep/result{i}.jpg")


#DONE: zatim zkusit vsechny classes dohromady, potom pripadne rozdelit na jednotlive tridy (bude potreba pregenerovat .txt, aby byla vzdy class 0)
#TODO: (az jistota, ze bude fungovat) aby generovalo primo tuto strukturu pri tvorbe dat
    # dataset/
    #     train1/
    #         images/
    #             .jpg
    #         labels/
    #             .txt
    #     train2/
    #     eval/
    #         images/
    #             .jpg
    #         labels/
    #             .jpg
    #     val
    #         images/
    #             .jpg
    #         labels/
    #             .jpg
    #     configEval.yaml
    #     configTrain1
    #     configTrain2


if __name__ == "__main__":
    main()