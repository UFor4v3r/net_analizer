pkgname=packet_sniffer_by_V01D
pkgver=1.0.0
pkgrel=1
pkgdesc="Advanced Packet Sniffer & Analysis Tool by V0iD"
arch=('any')
url="https://github.com/UFor4v3r/net_analizer"
license=('MIT')
depends=('python' 'python-scapy')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tar.gz::https://github.com/UFor4v3r/net_analizer/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
    cd "$srcdir/$pkgname-$pkgver"

    # Install using setup.py
    python setup.py install --root="$pkgdir/" --optimize=1
}
