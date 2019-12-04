from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    ads = Ads.objects.all()
    hotgames = HotGame.objects.all()
    gamevideos = GameVideo.objects.all()
    return render(request,'index.html',locals())
def about(request):
    cultures = Culture.objects.all()
    lifes = Life.objects.all()
    return render(request,'about.html',locals())
def contact(request):

    return render(request,'contact.html',locals())
def work(request):
    works = Work.objects.all()
    return render(request,'work.html',locals())
def join(request):
    # var
    # data = {
    #     kind: ["技术类", "策划类", "美术类", "市场类", "运营类", "品测类", "行政类"],
    #     gong: [["游戏客户端开发工程师", "游戏服务端开发工程师", "PHP开发工程师", "运维工程师", "网络管理员"], ["文案策划", "数值策划", "系统策划"],
    #            ["角色原画", "场景原画", "3D角色", "3D场景", "场景修图", "3D动作", "3D特效", "地编", "游戏UI", "广告设计"], ["手游投放推广", "市场策划"],
    #            ["游戏运营", "游戏商务", "游戏客服"], ["游戏测试"], ["招聘专员", "财务专员"]],
    #     infro1: [["1、参与游戏项目的整体技术工作与开发流程;<br>2、根据策划需求，负责游戏客户端功能的开发;<br>3、主动跟进与处理所负责模块的BUG;<br>4、按时完成上级主管交予的各项任务。",
    #               "1、游戏服务器网络、数据库引擎开发与维护;<br>2、游戏服务器框架设计与搭建;<br>3、优化系统性能，保证服务器质量和性能。",
    #               "1、对运营过程产生的数据进行管理、分析、处理等;<br>2、根据项目要求编写工具、生成报表、转化数据格式等;<br>3、负责多平台接口的对接工作。",
    #               "1、负责配置游戏运行环境，安装部署游戏;<br>2、游戏服务器的规划、监控，数据备份，日志分析，故障排除，性能调优等工作;<br>3、研究运维相关技术，根据系统需求制定运维技术方案;<br>4、研究系统架构、提高系统的健康性，参与运维流程制定、保证高效响应。",
    #               "1、负责公司内网外网系统的日常运行维护，保证网络运行畅通;<br>2、负责网络和系统的安全管理，做好数据安全和病毒防范工作;<br>3、定期备份关键数据和信息，保障电脑、打印机等电子设备的稳定运作;<br>4、及时采取有效措施严防网络病毒、网络黑客入侵，使用网络中心指定的存储设备和服务器交换数据，严防病毒感染。"],
    #              [
    #                  "1、游戏世界观架构或对IP进行游戏世界观解析重构;<br>2、游戏背景故事、任务故事、情节及对话设计编写;<br>3、系统和运营活动等各种游戏内文案包装;<br>4、任务功能跟进、任务撰写及任务配置。",
    #                  "1、根据游戏系统规则，进行系统底层框架的数学模型搭建和公式设计;<br>2、配合程序制定出数据及相关数值公式编写，确保可用性和扩展性强;<br>3、负责游戏中各种数值的调整，进行游戏的平衡性、持续可发展性等调整;<br>4、游戏各系统实现的数值支持，游戏系统数值平衡的演算。",
    #                  "1、游戏内各系统的功能设计、界面及操作设计;<br>2、游戏内各系统的内容和规则设计;<br>3、负责网络游戏 的策划资源管理、沟通协调，协调策划各个部分的协同工作。"],
    #              ["1、负责游戏角色、怪物、宠物等的原画设计与绘制;<br>2、负责项目宣传所需要的插图的绘画工作，必要时辅助进行图标设计与绘制。",
    #               "1、负责规划场景布局、制作;<br>2、各类细分场景、道具等的原画设计，把控整体场景设计的进度和质量。",
    #               "1、根据提供的原画高质量还原角色模型;<br>2、负责游戏内主角、NPC、BOSS、怪物等建模及贴图绘制。",
    #               "1、负责游戏内的建筑、植被等模型和贴图的制作;<br>2、负责游戏内场景杂物模型的贴图和制作。",
    #               "1、负责根据策划文档和2D场景确定的风格，对3D渲染的零部件及后期整图的修图工作;<br>2、参与设定及进行美术风格、制法研究，维护游戏美术品质。",
    #               "1、负责游戏中的角色和各类怪物动作设计与制作;<br>2、设计制作出流畅的角色动作。", "1、制作游戏中所需技能特效;<br>2、制作游戏中所需场景动画光效等特殊效果。",
    #               "1、负责游戏中关卡地图的设计;<br>2、负责U3D引擎中各类的场景地图的灯光烘焙、编辑制作等;<br>3、承担部分场景物件制作。",
    #               "1、游戏产品界面设计、优化产品界面用户体验;<br>2、系统功能图标、道具图标等手绘。",
    #               "1、根据公司及项目组要求制作市场投放广告图;<br>2、负责公司产品的落地页、icon等各种视觉元素的设计和制作;<br>3、负责公司产品的素材创意设计。"], [
    #                  "1、负责移动端手游广告的投放，确定合作渠道、准备投放素材、分析投放效果，对投放结果负责；<br>2、实时跟踪投放数据，结合数据对广告进行优化调整，完成广告数据统计分析，并多维度全面分析，根据分析结果优化投放策略。",
    #                  "1、掌握市场需求发展趋势，为游戏产品研发和投放推广提供支持；<br>2、负责游戏品牌宣传推广文案的策划、创意、撰写和执行。"], [
    #                  "1、负责制定各种线上运营活动，深度整合游戏产品，并根据客户需求及市场需求策划专题、活动等；<br>2、负责游戏平台日常维护和管理，对客服问题进行解答、整理，收集客服汇报用户建议及产品缺陷，推动产品质量持续改善。",
    #                  "1、负责渠道的开发，建设和维护，包括运营商渠道、第三方市场渠道，保证公司用户数量和合作伙伴的持续增长；<br>2、监控渠道数据，积极主动与渠道沟通，推动项目运作；<br>3、根据市场需求和自有资源，与渠道建立并保持正常稳定良好的关系，保证业务良好开展，及时把握渠道动向，拓展新的推广渠道。",
    #                  "1、负责在线处理用户的咨询、投诉、建议，确保信息传递的准确性和及时性，保证客户的满意度；<br>2、准确记录用户信息，按照规定的流程、标准正确记录用户的需求和建议；监控游戏运行状态，维护游戏世界的正常秩序；<br>3、及时反馈和协助处理游戏异常状况，并与玩家做好沟通。"],
    #              [
    #                  "1、负责游戏规则、功能与界面测试，查找、记录并跟踪处理BUG，及时反馈发现的问题；<br>2、负责反馈游戏可玩性、易玩性和系统性能，用例测试报告的编写，详细记录游戏测试过程，对BUG进行记录、跟踪处理和测试；<br>3、辅助策划优化和完善系统，特别是用户体验方面。"],
    #              ["1、根据招聘需求，选择招聘渠道，发布及更新招聘信息，完成简历的收集和初步筛选工作；<br>2、负责联系和接待候选人，安排面试事宜。",
    #               "1、负责公司日常会计核算，独立进行账务处理；<br>2、审核公司相关财务单据，编制各类财务报表，提供财务分析；<br>3、负责国税、地税各种税金的核实和上缴工作，每月按时编制上报各种税务报表；<br>4、完成公司安排的各项工作。"]],
    #     infro2: [[
    #                  "1、本科以上学历，计算机、软件相关专业;<br>2、有游戏项目开发经验者优先，熟悉cocos2d、cocos3d或Unity3D任意一项或以上，有完整项目开发经验者尤佳;<br>3、熟悉C/C++、Lua、Python等，具备良好的编程语言基础和编码习惯;<br>4、热爱游戏行业，对游戏制作有较好的见解;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，计算机、软件相关专业;<br>2、有游戏服务端开发经验、有erlang开发经验者优先，或精通C/C++、Lua、Java、Python等任一编程语言;<br>3、熟悉Linux环境，精通数据结构与算法，能够使用MySQL数据库进行应用开发;<br>4、热爱游戏行业，对游戏制作有较好的见解;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，计算机、软件相关专业;<br>2、有PHP开发经验者优先，精通PHP+MYSQL编程，精通PHP的面向对象编程，能够独立编写中等规模PHP应用程序;<br>3、熟练使用CI或thinkPHP框架，熟悉MYSQL数据库开发、配置、维护、性能优化;<br>4、良好的代码习惯，要求结构清晰、命名规范、逻辑性强，代码冗余率低;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，计算机、软件相关专业;<br>2、具有网游运维经验、大型网站运维经验者优先，精通Linux平台的业务维护，Nginx+mysql+php的配置、使用、调优;<br>3、了解Shell编程、熟悉PHP、Python语言任意一种优先;<br>4、对系统安全、入侵检测等有一定了解，能根据服务器的情况制定相应安全措施;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，计算机、软件相关专业;<br>2、精通计算机及相关IT设备的使用及维护，了解最新的计算机软、硬件产品，熟悉交换机、路由器、防火墙的原理及配置;<br>3、熟悉计算机及服务器硬件的安装、调试、熟悉网络交换、路由设备、熟悉数据备份系统，对网络安全有较深理解;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"],
    #              [
    #                  "1、本科及以上学历，专业不限;<br>2、熟悉游戏任务流程，有游戏文案工作经验者优先;<br>3、拥有较强文字功底、富有想象力，有写作作品者优先;<br>4、热爱游戏行业，游戏经历丰富，对游戏中的剧情文案有深入研究;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，专业不限;<br>2、有游戏数值策划相关工作经验，有RPG类型项目经验，或大型的成功项目经验优先;<br>3、具备良好的数据分析能力，扎实的数学建模和概率论等相关知识，能熟练操作office软件，特别是Excel中的函数应用;<br>4、热爱游戏行业，游戏经历丰富，对游戏中的数值有深入研究;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，专业不限;<br>2、有系统策划经验者优先，有广泛的游戏经验、大量的游戏积累，了解各时代各主机不同类型的单机、网络游戏;<br>3、熟悉游戏框架，熟悉游戏研发流程;<br>4、热爱游戏行业，游戏经历丰富，对游戏中的系统玩法有深入研究;<br>5、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"],
    #              [
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏原画制作经验者优先，具备扎实的美术基础与良好的手绘能力，熟悉人体、动物构造，熟悉原画设计及相关工作规范流程;<br>3、熟练掌握Photoshop、Painter等绘画相关软件，擅长设计不同特点任务角色、NPC、怪物;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏行业场景原画工作经验者优先，具备扎实的美术基础与良好的手绘能力，有较强的造型、色彩运用和创意能力;<br>3、熟悉场景设定流程，熟练掌握多种游戏美术风格，会修图和布局者优先;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏公司3D角色制作经验者优先，精通低精度模型创建，对高精度模型有一定认识;<br>3、精通3DSMAX、Photoshop、BodyPaint 3D等相关软件，熟悉人体造型结构。对各种类型动物形体有正确认识;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏公司3D场景制作经验者优先，能熟练运用3DSMAX与Photoshop、ZBrush等软件;<br>3、有良好的美术功底，熟悉掌握相关游戏场景制作软件三维建模方法、面数合理控制、布线合理分部与及准确材质贴图方法;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏场景设计及游戏修图从业经验者优先，有绘制“拼接”性场景元件相关工作经验者优先;<br>3、熟练使用PAINTER、PHOTOSHOP和手绘板等绘制软件，对游戏场景的建模和贴图绘制有相当的了解;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、具备3D游戏动作制作经验者优先，有相对完整的游戏动作制作经验，对动作有良好设计概念，对人物及不同生物的运动规律有一定的了解;<br>3、能熟悉U3D引擎者优先，熟练使用3DMAX进行角色骨骼的绑定及动画制作;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏公司3D特效制作经验者优先，能熟练使用3DMAX、AE等各种特效软件;<br>3、能熟悉U3D引擎者优先，具备较好的审美能力，有一定的手绘基础;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、参与过U3D项目美术设计开发，擅长3D类型的地图场景设计及编辑，构建并编辑场景;<br>3、对环境和空间的布局有较强能力，对地貌，建筑，植被有很好的表现能力;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有游戏UI相关工作经验者优先，熟练掌握Photoshop、illustrator等图形设计软件，有较强的界面设计能力;<br>3、有优秀的审美能力，独特的创意，有较强的平面设计和网页设计创意力，能良好地把握色彩搭配;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，美术相关专业优先;<br>2、有相关游戏广告设计经验者优先，熟练使用Photoshop、Illustrator、flash等设计软件，美术功底扎实;<br>3、熟知移动端主流平台的设计规范，对视觉用户研究有一定的经验和见解;<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"],
    #              [
    #                  "1、大专以上学历，专业不限；<br>2、熟悉移动广告投放流程，有手游广告投放经验者优先，熟悉竞价投放系统，有广点通、智汇推、今日头条、admob、inmobi等竞价系统；<br>3、熟悉ECXEL办公软件，对数据敏感，具备良好的数据分析能力和素材甄选能力，能完成各项投放考核指标；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专以上学历，专业不限；<br>2、有市场推广经验者优先，优秀应届生也可考虑，了解游戏行业市场动态，对市场趋势、数据敏感；<br>3、有较强的创造性思维能力、创意概念及良好的沟通能力，熟练使用数据分析及办公软件；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"],
    #              [
    #                  "1、本科及以上学历，专业不限；<br>2、有游戏运营工作经验优先，有较强的游戏感，对游戏活动策划有创意和实施经验；<br>3、对数据敏感，精通数据分析，有较强的逻辑思维能力，良好的综合协调能力，条理清晰，学习和总结能力强；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，专业不限；<br>2、有游戏商务经验者优先，拥有丰富的媒体资源和渠道推广资源优先；<br>3、熟悉游戏的各个流程，熟悉游戏市场，对行业发展有清晰认识，具备良好的业务拓展能力、渠道拓展能力，能在高压力下工作；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、大专及以上学历，专业不限；<br>2、有客服经验者优先，深入体验过至少一款游戏，熟悉游戏的系统玩法；<br>3、较好的沟通、表达、应变、协调及反应能力，较强的服务意识，较强的情绪自我控制及调节能力，能承受较强的工作压力，接受客服倒班工作性质；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"],
    #              [
    #                  "1、大专及以上学历，专业不限；<br>2、有游戏测试经验者优先，热爱并熟悉各种大型网络游戏，对游戏有独到的见解和敏锐的观察能力；<br>3、具备执行具体测试任务并确认测试结果、缺陷跟踪，完成测试报告以及测试结果分析能力；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"],
    #              [
    #                  "1、本科及以上学历以上，专业不限；<br>2、有互联网、游戏行业人力资源工作经验者优先，优秀应届毕业生亦可考虑，熟练使用办公软件，具备基本的网络知识；<br>3、思维清晰敏捷，具有较强的逻辑分析能力，具有良好的领悟分析解决问题的能力；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。",
    #                  "1、本科及以上学历，财务、会计相关专业，有会计从业资格证者优先；<br>2、有一般纳税人全盘账务处理操作经验者优先，熟悉会计法规和税法，熟练使用财务软件、Excel公式与函数及其他办公软件；<br>3、具有独立工作能力和财务分析能力；<br>4、良好的沟通能力与团队协作能力，高度的工作责任心和敬业精神。"]]
    # }
    data = {}
    ps = Position.objects.all()
    kind = []

    for p in ps:
        if p.type not in kind:
            kind.append(p.type)
    gong = []
    infro1 = []
    infro2 = []
    for k in kind:
        k_ps = ps.filter(type=k)
        k_g = []
        k_infro1 = []
        k_infro2 = []
        for k_p in k_ps:
            print(k_p)
            k_g.append(k_p.name)
            k_infro1.append(k_p.duty)
            k_infro2.append(k_p.require)
        gong.append(k_g)
        infro1.append(k_infro1)
        infro2.append(k_infro2)
    from .models import POSITION_TYPE
    kinds = []
    for k in kind:
        for pt in POSITION_TYPE:
            if k == pt[0]:
                kinds.append(pt[1])

    data = {"kind":kinds,"gong":gong,"infro1":infro1,"infro2":infro2}


    return render(request,'join.html',{"data":data})
def game(request):
    recommends = Recommend.objects.all()
    return render(request,'game.html',locals())