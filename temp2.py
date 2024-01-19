from bs4 import BeautifulSoup

html = """
<tr>
    <th scope="row">1247</th>
    <td>
        <dl>
            <dt>7번 염색체 장완 36 부분의 미세결손 증후군<p>7q36 microdeletion syndrome</p></dt>
            <dd>              
                <ul>
                    <li><span>항목분류 : </span>코드 없음</li>
                    <li><span>환자등록기준 : </span>산정특례 사전승인 신청 필요</li>
                    <li><span>의료비지원 :</span> 지원</li>
                    <li><span>KCD코드 :</span> 없음</li>
                    <li style="padding-left: 20px !important"><span>산정특례 특정기호 :</span> V901</li>
                </ul>
            </dd>
        </dl>
    </td>
    <td>
        <a href="#" onclick="javascript:fn_moveDetail('RA201910076'); return false;" title="질환정보 바로가기" style="height: 120.969px;"><span>질환정보 바로가기</span></a>
    </td>
</tr>
"""

soup = BeautifulSoup(html, 'html.parser')

# 제목 추출 (한국어, 영어)
dt = soup.select_one('dt')
if dt:
    p = dt.find('p')
    if p:
        title_en = p.get_text(strip=True)
        p.extract()
    title_ko = dt.get_text(strip=True)
else:
    title_ko = ''
    title_en = ''

# KCD 코드 추출
li_kcd = soup.select_one('dd > ul > li:nth-child(4)')
kcd = li_kcd.get_text(strip=True).split(':')[-1].strip() if li_kcd else ''

# 산정특례 특정기호 추출
li_spc_code = soup.select_one('dd > ul > li:nth-child(5)')
spc_code = li_spc_code.get_text(strip=True).split(':')[-1].strip() if li_spc_code else ''

# 항목 분류 추출
li_group = soup.select_one('dd > ul > li:nth-child(1)')
group = li_group.get_text(strip=True).split(':')[-1].strip() if li_group else ''

# 의료비 지원 여부 추출
li_support = soup.select_one('dd > ul > li:nth-child(3)')
support = li_support.get_text(strip=True).split(':')[-1].strip() if li_support else ''

# 결과 출력
print(f"제목 (한국어): {title_ko}")
print(f"제목 (영어): {title_en}")
print(f"KCD 코드: {kcd}")
print(f"산정특례 특정기호: {spc_code}")
print(f"항목 분류: {group}")
print(f"의료비 지원 여부: {support}")
