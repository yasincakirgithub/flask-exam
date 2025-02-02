from app import create_app
from app.extensions import db
from app.models import Question, AnswerType

# Flask uygulamasını başlat
app = create_app()
app.app_context().push()


def add_example_data():

    questions = [
        Question(
            queue=1,
            text="Python'da yapay zeka modelleri geliştirmek için en yaygın kullanılan iki kütüphane nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="TensorFlow ve PyTorch",
        ),
        Question(
            queue=2,
            text="Scikit-learn kütüphanesinin temel olarak hangi tür makine öğrenmesi problemlerini çözmek için kullanıldığını belirtin.",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Denetimli öğrenme",
        ),
        Question(
            queue=3,
            text="Python'da bir modelin hiperparametrelerini optimize etmek için hangi yöntemler kullanılabilir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Grid Search ve Random Search",
        ),
        Question(
            queue=4,
            text="Python'da derin öğrenme modellerini eğitmek için hangi kütüphaneleri kullanabilirsiniz?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="TensorFlow ve PyTorch",
        ),
        Question(
            queue=5,
            text="Python'da yapay zeka için model değerlendirme metriklerinden biri nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Doğruluk (Accuracy)",
        ),
        # Bilgisayar Görüşü
        Question(
            queue=6,
            text="Python'da görüntü işleme ve bilgisayar görüşü uygulamaları için yaygın olarak kullanılan kütüphane nedir?",
            answer_type=AnswerType.choice,
            a="OpenCV",
            b="NumPy",
            c="Matplotlib",
            d="SciPy",
            ans="OpenCV",
        ),
        Question(
            queue=7,
            text="Bir görüntüde kenarları tespit etmek için hangi algoritma sıkça kullanılır?",
            answer_type=AnswerType.choice,
            a="Sobel",
            b="K-means",
            c="Principal Component Analysis",
            d="DBSCAN",
            ans="Sobel",
        ),
        Question(
            queue=8,
            text="Hangi derin öğrenme yapısı, nesne tanıma görevlerinde genellikle kullanılır?",
            answer_type=AnswerType.choice,
            a="Recurrent Neural Networks (RNN)",
            b="Convolutional Neural Networks (CNN)",
            c="Generative Adversarial Networks (GAN)",
            d="Long Short-Term Memory (LSTM)",
            ans="Convolutional Neural Networks (CNN)",
        ),
        Question(
            queue=9,
            text="Bir görüntüde yüz tanıma yapmak için hangi model türü en uygundur?",
            answer_type=AnswerType.choice,
            a="K-Nearest Neighbors (KNN)",
            b="Support Vector Machine (SVM)",
            c="FaceNet",
            d="Naive Bayes",
            ans="FaceNet",
        ),
        Question(
            queue=10,
            text="Python'da görüntü segmentasyonu için hangi teknikler kullanılır?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="U-Net ve Mask R-CNN",
        ),
        # NLP (Doğal Dil İşleme)
        Question(
            queue=11,
            text="BERT ve GPT modelleri hangi tür doğal dil işleme görevlerinde kullanılır?",
            answer_type=AnswerType.choice,
            a="Metin sınıflandırma ve özetleme",
            b="Görüntü segmentasyonu",
            c="Ses tanıma",
            d="Zaman serisi tahmini",
            ans="Metin sınıflandırma ve özetleme",
        ),
        Question(
            queue=12,
            text="Tokenization nedir ve neden önemlidir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Tokenization, metni kelime veya alt kelime birimlerine ayırır ve NLP modellerinin işleme almasını kolaylaştırır.",
        ),
        Question(
            queue=13,
            text="LSTM ağları hangi tür görevler için genellikle kullanılır?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Zaman serisi tahmini ve dil modelleme",
        ),
        Question(
            queue=14,
            text="Bir metni özetlemek için hangi tür model genellikle kullanılır?",
            answer_type=AnswerType.choice,
            a="Sequence-to-Sequence (Seq2Seq)",
            b="Convolutional Neural Network (CNN)",
            c="Recurrent Neural Network (RNN)",
            d="Generative Adversarial Network (GAN)",
            ans="Sequence-to-Sequence (Seq2Seq)",
        ),
        Question(
            queue=15,
            text="Bir metni özetlemek için hangi model sıklıkla kullanılmaktadır?",
            answer_type=AnswerType.choice,
            a="BERT",
            b="Transformer",
            c="GPT",
            d="CNN",
            ans="BERT",
        ),
        # Python Uygulamalarında AI Modelleri Uygulama
        Question(
            queue=16,
            text="Flask veya Django ile bir yapay zeka modelini entegre etmek mümkün müdür?",
            answer_type=AnswerType.yes_no,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="yes",
        ),
        Question(
            queue=17,
            text="Python uygulamalarında yapay zeka modelini gerçek zamanlı olarak çalıştırmak için en uygun yöntemlerden biri, modelin web servislerine dönüştürülmesidir.",
            answer_type=AnswerType.yes_no,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="yes",
        ),
        Question(
            queue=18,
            text="REST API kullanarak bir yapay zeka modeline erişim sağlamak için hangi kütüphane yaygın olarak kullanılır?",
            answer_type=AnswerType.choice,
            a="Flask",
            b="NumPy",
            c="OpenCV",
            d="Matplotlib",
            ans="Flask",
        ),
        Question(
            queue=19,
            text="Bir yapay zeka modelini Python uygulamasına entegre etmek için hangi format sıklıkla kullanılır?",
            answer_type=AnswerType.choice,
            a="CSV",
            b="JSON",
            c="XML",
            d="YAML",
            ans="JSON",
        ),
        Question(
            queue=20,
            text="Bir Python uygulamasında yapay zeka modelinin performansını değerlendirmek için hangi metrikler kullanılır?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Doğruluk, Precision, Recall, F1 Skoru",
        ),
        # Devamı
        Question(
            queue=21,
            text="Python'da veri ön işleme adımlarından biri nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Ölçekleme (Scaling)",
        ),
        Question(
            queue=22,
            text="Convolutional Neural Networks (CNN) hangi tür veri ile en iyi sonuçları verir?",
            answer_type=AnswerType.choice,
            a="Zaman serisi verisi",
            b="Metin verisi",
            c="Görüntü verisi",
            d="Tablo verisi",
            ans="Görüntü verisi",
        ),
        Question(
            queue=23,
            text="RNN'lerin temel avantajı nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Zaman serisi verilerini ve dizilim verilerini işleme yeteneği",
        ),
        Question(
            queue=24,
            text="Bir modelin overfitting problemini nasıl çözebilirsiniz?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Regularization, veri artırma, ve erken durdurma kullanarak",
        ),
        Question(
            queue=25,
            text="NLP'de 'stemming' ve 'lemmatization' arasındaki temel fark nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Stemming kökleri kısaltırken, lemmatization dil bilgisel olarak doğru kelime köklerini bulur.",
        ),
        Question(
            queue=26,
            text="Bir metin verisinde stop-words'leri kaldırmak hangi adımın bir parçasıdır?",
            answer_type=AnswerType.choice,
            a="Tokenization",
            b="Stopword Removal",
            c="Stemming",
            d="Lemmatization",
            ans="Stopword Removal",
        ),
        Question(
            queue=27,
            text="Hangi model yapısı genellikle dil modelleme ve metin üretme için kullanılır?",
            answer_type=AnswerType.choice,
            a="CNN",
            b="RNN",
            c="KNN",
            d="SVM",
            ans="RNN",
        ),
        Question(
            queue=28,
            text="Veri kümesinde eksik verileri işlemek için hangi yöntemler kullanılabilir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Eksik değerleri ortalama, medyan veya mod ile doldurmak",
        ),
        Question(
            queue=29,
            text="Python'da model tahminleri için en yaygın kullanılan kütüphanelerden biri nedir?",
            answer_type=AnswerType.choice,
            a="Flask",
            b="PyTorch",
            c="OpenCV",
            d="NumPy",
            ans="PyTorch",
        ),
        Question(
            queue=30,
            text="Bir modelin eğitim süresini kısaltmak için hangi teknikleri kullanabilirsiniz?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Modeli küçültmek, daha hızlı donanım kullanmak, batch size'ı artırmak",
        ),
        Question(
            queue=31,
            text="Kümeleme algoritmalarından biri nedir?",
            answer_type=AnswerType.choice,
            a="K-Means",
            b="Linear Regression",
            c="Decision Tree",
            d="Logistic Regression",
            ans="K-Means",
        ),
        Question(
            queue=32,
            text="Ensemble öğrenme yöntemleri neyi ifade eder?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Birden fazla modelin birleştirilerek daha iyi sonuçlar elde edilmesi",
        ),
        Question(
            queue=33,
            text="Veri normalizasyonu neden önemlidir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Modelin daha hızlı ve daha doğru eğitim almasını sağlar.",
        ),
        Question(
            queue=34,
            text="Derin öğrenme modellerinde hangi optimizasyon algoritmaları yaygın olarak kullanılır?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Adam, SGD, RMSprop",
        ),
        Question(
            queue=35,
            text="Bir yapay zeka modelinin kararlarını açıklamak için kullanılan terim nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Model interpretability",
        ),
        Question(
            queue=36,
            text="Bir modelin performansını değerlendirmek için çapraz doğrulama nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Veri setini birkaç alt kümeye bölerek modelin her bir alt kümede test edilmesi.",
        ),
        Question(
            queue=37,
            text="İnce ayar yapmak ne anlama gelir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Önceden eğitilmiş bir modeli belirli bir görev için tekrar eğitmek.",
        ),
        Question(
            queue=38,
            text="Sık kullanılan bir veri görselleştirme kütüphanesi nedir?",
            answer_type=AnswerType.choice,
            a="Matplotlib",
            b="SciPy",
            c="OpenCV",
            d="TensorFlow",
            ans="Matplotlib",
        ),
        Question(
            queue=39,
            text="En yaygın kullanılan sınıflandırma algoritmalarından biri nedir?",
            answer_type=AnswerType.choice,
            a="K-Nearest Neighbors (KNN)",
            b="Principal Component Analysis (PCA)",
            c="K-Means",
            d="Linear Regression",
            ans="K-Nearest Neighbors (KNN)",
        ),
        Question(
            queue=40,
            text="Yapay zeka modellerinin eğitim sürecini hızlandırmak için hangi donanım kullanılır?",
            answer_type=AnswerType.choice,
            a="CPU",
            b="GPU",
            c="RAM",
            d="HDD",
            ans="GPU",
        ),
        Question(
            queue=41,
            text="Bir yapay zeka modelini Python'da bir API olarak sunmak için hangi kütüphane kullanılabilir?",
            answer_type=AnswerType.choice,
            a="Flask",
            b="TensorFlow",
            c="Scikit-learn",
            d="NumPy",
            ans="Flask",
        ),
        Question(
            queue=42,
            text="Doğal dil işleme (NLP) modellerinde 'token' nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Metin içindeki kelime veya karakter birimi",
        ),
        Question(
            queue=43,
            text="Bir modelin eğitim veri setinden türetme hatasını anlamak için kullanılan kavram nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Overfitting",
        ),
        Question(
            queue=44,
            text="Hangi model tipi sıklıkla 'regression' analizi için kullanılır?",
            answer_type=AnswerType.choice,
            a="Decision Tree",
            b="Logistic Regression",
            c="Linear Regression",
            d="K-Nearest Neighbors",
            ans="Linear Regression",
        ),
        Question(
            queue=45,
            text="Bir modelin performansını değerlendirmek için kullanılan metriklerden biri nedir?",
            answer_type=AnswerType.choice,
            a="Confusion Matrix",
            b="Frequency Histogram",
            c="ROC Curve",
            d="Precision-Recall Curve",
            ans="Confusion Matrix",
        ),
        Question(
            queue=46,
            text="Bert ve GPT modelleri hangi teknolojiye dayanır?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Transformer",
        ),
        Question(
            queue=47,
            text="Derin öğrenme uygulamalarında modelin genel performansını değerlendirmek için kullanılan kütüphane nedir?",
            answer_type=AnswerType.choice,
            a="Scikit-learn",
            b="TensorBoard",
            c="OpenCV",
            d="Keras",
            ans="TensorBoard",
        ),
        Question(
            queue=48,
            text="AI tabanlı bir modelin eğitim sürecini hızlandırmak için kullanılan bir teknik nedir?",
            answer_type=AnswerType.single_line,
            a=None,
            b=None,
            c=None,
            d=None,
            ans="Transfer Learning",
        ),
        Question(
            queue=49,
            text="Bir modelin performansını izlemek için kullanılan araçlardan biri nedir?",
            answer_type=AnswerType.choice,
            a="Jupyter Notebook",
            b="TensorFlow Serving",
            c="AWS S3",
            d="Django Admin",
            ans="TensorFlow Serving",
        ),
        Question(
            queue=50,
            text="Bir yapay zeka modelinin eğitilmesi sırasında hiperparametre optimizasyonu yapmak için hangi kütüphane kullanılır?",
            answer_type=AnswerType.choice,
            a="Optuna",
            b="NumPy",
            c="Matplotlib",
            d="Flask",
            ans="Optuna",
        ),
    ]

    with app.app_context():
        db.session.add_all(questions)
        db.session.commit()
        print("Örnek veriler başarıyla eklendi.")


if __name__ == "__main__":
    add_example_data()
