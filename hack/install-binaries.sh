
# colors
green='\033[0;32m'
blue='\033[0;34m'
reset='\033[0m'

install_binaries() {
	echo "${blue}INSTALL BINARIES${reset}"

	local kubectl_version=1.29.0
	local kind_version=0.22.0

	# bin directory
	local bin="${root}/bin"
	mkdir -p ${bin}

	install_kubectl
	install_kind

	echo ${green}DONE${reset}
}

install_kubectl() {
 echo "${blue}> kubectl${reset}"

	curl -sSLo "${bin}"/kubectl "https://dl.k8s.io/release/v${kubectl_version}/bin/linux/amd64/kubectl"
	chmod +x "${bin}"/kubectl
	"${bin}"/kubectl version
 
}

install_kind() {
	#echo "${blue}> kind${reset}"

}
