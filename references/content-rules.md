
## Mod (modification) iddiaları KALDIRILIR

Bulut oturumunda kullanıcının dosya sistemine erişimi yok ve mod desteği oyundan oyuna değişiyor.
Özellikle **"sonraki oturumlarda korunur"** bir kalıcılık vaadidir; kullanıcı buna güvenip abone
olur ve modları bulamazsa doğrudan beklenti kırılması olur. Bu yüzden modification iddiaları
içerikten çıkarılır (`MOD_CUMLE` ve `FAQ_KALDIR`, `port_category_v11.py`).

**Türkçe tuzağı:** "mod" hem *game mode* hem *modification* demek. Yalnızca modification
iddiaları kaldırılır; **"rekabetçi modlar", "çok oyunculu modlar", "Horde ve Escape modları"
gibi OYUN MODU ifadelerine DOKUNULMAZ.** İlk taramada 65 eşleşmenin yalnız 10'u gerçek
modification iddiasıydı.

**Kütüphanede yer alan bir yapımın adı mod içerse de kalır** (ör. "Portal: Prelude RTX (topluluk
modu)") - bu bir katalog kaydıdır, mod desteği vaadi değil.

**Bilinçli kaldırma, korunum kontrolünün dışında tutulur:** aynı temizlik
`verify_source_preserved`ın karşılaştırma temeline de uygulanır; yoksa kasıtlı silme "metin kaybı"
olarak raporlanır ve gerçek kayıpları maskeler.
